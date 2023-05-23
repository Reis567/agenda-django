from django.shortcuts import render
from contact.forms import RegisterForm
# flake8: noqa

# Create your views here.


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

    return render(
        request,
        'contact/register.html',
        {
            'form':form
        },
    )