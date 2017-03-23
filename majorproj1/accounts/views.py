from django.shortcuts import render,redirect	
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt	
from app01.models import LoginForm,RegisterForm
from models import MyUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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
	print frm.cleaned_data
	if frm.is_valid():
		
		uname = frm.cleaned_data['username']
		ps = frm.cleaned_data['password']
		name = frm.cleaned_data['name']
		try:
			usr= User(username=uname)
			usr.set_password(ps)
			usr.save()
			

		except:
			resp['status']='user already exists'
			return HttpResponse(json.dumps({'data':resp}))

		myusr = MyUser(user=usr,name=name)
		myusr.save()
		
		resp['status'] = 'success'
		return HttpResponse(json.dumps({'data':resp}))
	else:
		resp['status'] = 'enter valid form'
		return HttpResponse(json.dumps({'data':resp}))
@csrf_exempt
def user_login(request):
	
	resp = {
		'status': ''
	}

	if not request.method == 'POST':
		resp['status'] = 'Y U NO POST REQUEST?'
		return HttpResponse(json.dumps({'data': resp}))
	print request.POST
	frm1 = LoginForm(request.POST)
	print frm1

	if frm1.errors:
		for field in frm1:
			for error in field.errors:
				print error

	if frm1.is_valid():
		print 'yes', frm1.cleaned_data
		uname = frm1.cleaned_data['usrname']
		ps = frm1.cleaned_data['passwd']

		u = authenticate(username=uname, password=ps)
		print u

		if u:
			if u.is_active:
				login(request, u)
				print u
				# ctx = {'user': u}
				resp['status'] = 'success';
				return HttpResponse(json.dumps({'data': resp}))
				# return render(request, 'logged_in.html')#, ctx)
			else:
				resp['status'] = 'Deactivcated account';
				return HttpResponse(json.dumps({'data': resp}))
		else:
			resp['status'] = 'Invalid User!';
			return HttpResponse(json.dumps({'data': resp}))
	else:
		resp['status'] = 'Invalid Form Data!!';
		return HttpResponse(json.dumps({'data': resp}))

@login_required
def user_logout(request):
	print request.user
	logout(request)
	return redirect('/')