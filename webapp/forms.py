from .models import formDetails
from django import forms

class detailsForm(forms.ModelForm):
    class Meta:
        model=formDetails
        fields='__all__'