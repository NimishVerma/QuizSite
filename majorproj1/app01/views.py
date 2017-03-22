from django.shortcuts import render, redirect
from django.http import HttpResponse
from models import RegisterForm, LoginForm
from django.views.decorators.csrf import csrf_protect

# Create your views here.

def main(request):
	rfrm = RegisterForm()
	lfrm = LoginForm()
	ctx = {'rform' : rfrm,
			'lform' : lfrm}
	return render(request,"index.html",ctx)
