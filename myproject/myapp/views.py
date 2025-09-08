from django.shortcuts import render
from myapp.forms import RegisterForm
from .models import Register

def landpage(req):
    return render(req, 'register.html')

def register(req):
    if req.method=='POST':
        form=RegisterForm(req.POST,req.FILES)
        if form.is_valid():
            n=form.cleaned_data['name']
            print(n)
    fm = RegisterForm()
    return render(req, 'register.html', {'x': fm})