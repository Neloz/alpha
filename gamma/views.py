from django.http import HttpResponse
from django.shortcuts import render, redirect
from usuarios.models import Tran
import requests
import json

def home(request):
    template_name = 'index.html'
    if 'status' in request.session:
        if request.session['status']=='success':
            r = requests.get('http://192.168.2.133:8050/api/transactions')
            trans = json.loads(r.text)

        else:
            return HttpResponse('''
            <h1>Tu no estas autorizado</h1> <br/>
            <p>
            <a class="nav-link" href="accounts/login">Login in</a>
            </p>


            '''
            )
    else:
        return redirect('accounts/login')

def detalles(request):
    template_name = 'detalle.html'
    return render(request, template_name)
