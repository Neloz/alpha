import json
import urllib.request
import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from usuarios.forms import LoginForm
from django.http import HttpResponse
from .models import Users


class LoginIn(TemplateView):
	template_name = 'usuarios/login.html'

	def get(self, request):
		form = LoginForm()
		return render(request, self.template_name, {'form':form})

	def post(self, request):
		form = LoginForm(request.POST)
		if form.is_valid():
			#text = []
			text = form.data
			#text = json.dumps(text)
			r = requests.post('http://192.168.2.133:8050/api/login', data=text)
			python_obj = json.loads(r.text)

			if r.status_code == 200:
				request.session['username'] = python_obj['data']['name']
				request.session['email'] = python_obj['data']['email']
				request.session['status'] = python_obj['status']
			else:
				request.session['status'] = 'unauthorizated'
				var = True
				return render(request, self.template_name, {'form':form, 'var':var})

		else:
			request.session['status'] = 'unauthorizated'
			var_session = 'unauthorizated'
			return render(request, self.template_name, {'form':form})

		return redirect('home')

def logout(request):
	return redirect('http://sso.trust.lat/oxauth/restv1/end_session')
