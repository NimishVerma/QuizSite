from django.shortcuts import render,redirect	
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt	
from app01.models import LoginForm,RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import json
# Create your views here.
@csrf_exempt
def register_data(request):
	resp = {
		'status': ''
	}

	if not request.method == 'POST':
		resp['status'] = 'post req pls'
		return HttpResponse(json.dumps({'data': resp}))

	frm = RegisterForm(request.POST)

	if frm.is_valid():
		
		uname = frm.cleaned_data['username']
		ps = frm.cleaned_data['password']
		name = frm.cleaned_data['name']
		try:
			usr= User(username=uname)
			usr.set_password(ps)
			usr.save()
			

		except:
			resps['status']='user already exists'
			return HttpResponse(json.dumps({'data':resp}))

		myusr = MyUser(user=usr,name=name)
		myusr.save()
		return redirect('/')
		resp['status'] = 'success'
		return HttpResponse(json.dumps({'data':resp}))

