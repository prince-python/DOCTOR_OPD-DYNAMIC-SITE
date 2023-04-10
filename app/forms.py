from django.core import validators
from django import forms
from . models import *


class activityform(forms.ModelForm):
    class Meta:
        model = activity
        fields = '__all__'
        # fields = '__all__'
        # exclude = ['name']
        wigdets = {
            
            'date':forms.DateTimeField(),
           
        }
