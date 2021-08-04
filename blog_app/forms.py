from . models import *
from django import forms

class ModeForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['name','img','desc']