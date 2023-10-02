from django import forms
from .models import *

class ProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ['name', 'client', 'users', 'start_date', 'end_date']