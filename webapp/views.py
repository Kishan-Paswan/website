from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import auth,messages
from django.contrib.auth import authenticate,logout
from .models import formDetails
from .forms import detailsForm
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q


def home(request):
    return render(request,'webapp/index.html')


def signup(request):
    form = UserCreationForm()
    success = False 
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            success = True
        else:
            messages.error(request, 'Error in form submission. Please check the form and try again.')

    context = {'form': form, 'success': success}
    return render(request, 'webapp/index.html', context)

 
def login(request):
    form = AuthenticationForm()
    if request.method=='POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user = authenticate(request, username=username,password=password)

            if user is not None:
                auth.login(request,user)
                return redirect('dashboard')
            else:
                print(username,password)
    return render(request,'webapp/index.html') 

@login_required(login_url='login') 
def dashboard(request):
     form=formDetails()
     details=formDetails.objects.filter(user=request.user)
     context={'form':form, 'data':details}
     if request.method=='POST':
      submitDetails = detailsForm(request.POST , request.FILES)
      if submitDetails.is_valid():
          submitDetails.save()
          messages.success(request, 'Details submitted successfully!')
          return redirect('dashboard')
      else:
           
         for field, errors in submitDetails.errors.items():
              for error in errors:
                 messages.error(request, f'{field.capitalize()}: {error}')           
     return render(request, 'webapp/dashboard.html', context)

def dashboard_logout(request):
    logout(request)
    return redirect('login')
     


def update(request, id):
    details = formDetails.objects.filter(user=request.user)
    editedData = formDetails.objects.get(user=request.user, id=id)

    if request.method == 'POST':
        print(request.POST)
        
        form = detailsForm(request.POST, request.FILES, instance=editedData)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form details successfully updated!')
            return redirect('dashboard')
        else:
            print(form.errors)
            messages.error(request,'errror in your code')
    context = { 'data':details ,'update': editedData }
    return render(request, 'webapp/update.html', context)

def delete(request, id):
    deletedData = formDetails.objects.get(user=request.user, id=id)
    deletedData.delete()
    messages.success(request, 'Form details successfully deleted!')
    return redirect('dashboard')
        
def search(request):
    context = {'data': None}
    if request.method=='POST':
        query= request.POST.get('query')
        try:
            id_query = int(query)
            details = formDetails.objects.filter(Q(id=id_query))
        except ValueError:      
            details = formDetails.objects.filter(
                Q(name__icontains=query) |
                Q(dob__icontains=query) |
                Q(email__icontains=query) |
                Q(mobile__icontains=query) |
                Q(address__icontains=query)
            )  
        context={'data':details}
    return render(request,'webapp/search.html' ,context)