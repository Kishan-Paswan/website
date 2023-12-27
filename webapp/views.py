from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from webapp.models import gallary,sign,jobmodel,contactmodel,servicesmodel,userservices
from webapp.form import signForm




# Create your views here.
def signfunction(request):
    data= sign.objects.all()
    context={'data': data}
    return render(request, 'register.html', context)

              

def signupuser(request):
    if request.method=="POST":
        Username=request.POST.get('Username')
        Email=request.POST.get('Email')
        Password=request.POST.get('Password')
        Phone=request.POST.get('Phone')
        Address=request.POST.get('Address')
        
        sn=sign(Username=Username,Email=Email,Password=Password,Phone=Phone,Address=Address)
        sn.save()
        
        return redirect('/login')
   

def logfunction(request):
   if request.method=="POST":
       Username=request.POST.get('Username')
       Password=request.POST.get('Password')
       user=authenticate(request,Username=Username,Password=Password)
       if user is not None:
           login(request,user)
           return redirect('home')
       else:
           return HttpResponse("username or password is incorrect ")
               
   return render(request,'login.html')
       
    
       
   
 
def log(request):
    return render(request,'index.html')
 
   

    

def home(request):
    return render(request,'index.html')

def aboutfunction(request):
    return render(request,'aboutus.html')

def gallaryfunction(request):
    data= gallary.objects.all()
    context={'data': data}
    return render(request,'gallary.html',context)

def contactfunction(request):
    return render(request,'contact-us.html')
def contactf(request):
    if request.method=="POST":
        Username=request.POST.get('Username')
        Email=request.POST.get('Email')
        
        Phone=request.POST.get('Phone')
        Message=request.POST.get('Message')
        ctn=contactmodel(Username=Username,Email=Email,Phone=Phone,Message=Message)
        ctn.save()
        return render(request,'index.html')

    

def job(request):
    return render(request,'job.html')

def jobfunction(request):
    if request.method=="POST":
        Name=request.POST.get('Name')
        Phone=request.POST.get('Phone')
        Email=request.POST.get('Email')
        Resume=request.POST.get('Resume')
        Pic=request.POST.get('Pic')
        Password=request.POST.get('Password')
        
        
        jb=jobmodel(Name=Name,Phone=Phone,Email=Email,Resume=Resume,Pic=Pic,Password=Password)
        jb.save()
        

        return render(request,'index.html')
def thanku(request):
    return render(request,'thanku.html')
    
def services(request):
    data=servicesmodel.objects.all()
    context={'data':data}
    return render(request,'services.html',context)    
        
def details(request,id):
    data=servicesmodel.objects.get(id=id)
    context={'data':data}
    return render(request,'details.html',context)
def userservice(request):
    sid=request.POST.get('sid')
    
    pic=request.POST.get('pic')
    title=request.POST.get('title')
    Name=request.POST.get('Name')
    Phone=request.POST.get('Phone')
    Email=request.POST.get('Email')
    Address=request.POST.get('Address')
    Message=request.POST.get('Message')
    userser=userservices(sid=sid,pic=pic,title=title,Name=Name,Phone=Phone,Email=Email,Address=Address,Message=Message)
    userser.save()

    return render(request,'thanku.html')
        
def myaccount(request):
    data= userservices.objects.all()
    
    context={'data': data}
    return render(request, 'myaccount.html',context)

def destroy(request, id):  
    mdata = userservices.objects.get(id=id)  
    mdata.delete()  
    data= userservices.objects.all()
    return render(request,'myaccount.html', {'data': data}) 
        