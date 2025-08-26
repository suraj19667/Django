from django import forms

class RegisterForm(forms.Form):

    name=forms.CharField()
    email=forms.EmailField()
    contact=forms.IntegerField()
    image=forms.ImageField()
    file=forms.FileField()
    