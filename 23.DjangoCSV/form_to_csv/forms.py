from django import forms
from django.db.models import fields 
from .models import CSVStore
# creating a form  
class InputForm(forms.ModelForm):
    class Meta:
        model = CSVStore
        fields = ['user_name', 'user_text']
        
