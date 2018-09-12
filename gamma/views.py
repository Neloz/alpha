from django.http import HttpResponse
from django.shortcuts import render, redirect

def home(request):
    template_name = 'index.html'
    if 'status' in request.session:
        if request.session['status']=='success':
            return render(request, template_name)
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
