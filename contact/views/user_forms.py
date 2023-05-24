from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
from contact.forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
# flake8: noqa

# Create your views here.


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'Usuário registrado')
            return redirect('contact:index')

    return render(
        request,
        'contact/register.html',
        {
            'form':form
        },
    )


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request , data = request.POST)

        if form.is_valid():
            user = form.get_user()
            messages.success(request,'Login realizado')
            auth.login(request, user)
            return redirect('contact:index')
        else:
            messages.error(request , "Credenciais invalidas")

    return render(
        request,
        'contact/login.html',
        {
            'form':form
        },
    )

def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')