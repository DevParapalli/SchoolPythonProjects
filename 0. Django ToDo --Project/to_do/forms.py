
from django import forms
from django.forms import widgets
from .models import ToDo

class ToDoForm(forms.ModelForm):
    
    
    class Meta:
        model=ToDo
        fields=('title', 'data', 'dead_line')
        excludes=("is_done")
        widgets = {
            'dead_line': widgets.DateTimeInput(attrs={'required': True, 'placeholder':'DD/MM/YYYY HH:MM[:SS]'})
        }
        