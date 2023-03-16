from django import forms
from .models import *

class profile(forms.ModelForm):
    class meta():
        model=Post
        fields="__all__"