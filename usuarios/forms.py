from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django import forms

class LoginForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField()
