from django import forms
from webapp.models import sign
from webapp.models import jobmodel
from webapp.models import contactmodel
from webapp.models import userservices


class signForm(forms.ModelForm):

    class Meta:  
        model = sign
        fields='__all__' 


class jobForm(forms.ModelForm):

     class Meta:  
         model = jobmodel
         fields='__all__'

class contactForm(forms.ModelForm):

     class Meta:  
         model = contactmodel
         fields='__all__'

class contactForm(forms.ModelForm):

     class Meta:  
         model = userservices
         fields='__all__'                                    