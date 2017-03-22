from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django import forms



class RegisterForm(forms.Form):
	name = forms.CharField(max_length=50,label='Your Name')
	username = forms.CharField(max_length=20, label='Username')
	password = forms.CharField(widget=forms.PasswordInput(), label ='your password')
class LoginForm(forms.Form):
	username = forms.CharField(max_length=20, label='Username')
	passwd = forms.CharField(widget=forms.PasswordInput(), label='your password')

	

