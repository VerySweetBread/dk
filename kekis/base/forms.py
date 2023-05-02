from django import forms
from .models import *


class LoginForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['login', 'password']