from django.shortcuts import render
# flake8: noqa

# Create your views here.
def index(request):
    return render(
        request,
        'contact/index.html',
    )