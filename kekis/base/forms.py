from django import forms
from .models import *


class LoginForm(forms.Form):
    login = forms.CharField(max_length=40, label="Login", widget=forms.TextInput(attrs={'class': 'input-field'}))
    password = forms.CharField(max_length=40, label="Password", widget=forms.TextInput(attrs={'class': 'input-field', 'type': 'password'}))