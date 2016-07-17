from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout


def login_page(request):
    message = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    message = "Te has identificado de modo correctamente"
                    return redirect('contabilidad.views.index_view')
                else:
                    message = "Tu usuario esta inactivo"
            else:
                message = "Nombre de usuario y/o password incorrecto"
    else:
        form = LoginForm()


    return render_to_response('production/login.html', {'message': message, 'form': form},context_instance=RequestContext(request))



def prueba(request):
    return render_to_response("production/base.html", context_instance=RequestContext(request))

def index2(request):
    return render_to_response("production/index2.html", context_instance=RequestContext(request))

def tables_dynamic2(request):
    return render_to_response("production/tables_dynamic2.html", context_instance=RequestContext(request))

def chartjs(request):
    return render_to_response("production/chartjs.html", context_instance=RequestContext(request))




def logout_view(request):
    logout(request)
    return redirect('login')


