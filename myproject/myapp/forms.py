from django import forms
from django.core.exceptions import ValidationError

class RegisterForm(forms.Form):

    name=forms.CharField()
    email=forms.EmailField()
    contact=forms.IntegerField()
    image=forms.ImageField()
    file=forms.FileField()
    
# ------ Field Level Validation ------

    def clean(self):
        print("End of Name_Validation from forms.py")
        name=self.cleaned_data('name')
        print(name)
        print(type(name))
        if len(name)==0:
            raise forms.ValidationError("Name cannot be empty")
        elif name.isdigit():
            raise forms.ValidationError("Name should not contain numbers")
        elif name[0].isdigit():
            raise forms.ValidationError("Name should not start with a number")
        elif not (name.isalpha() and len(name)<20 and len(name)>3):
            raise forms.ValidationError("Name should contain only alphabets")
        return name
    
    def clean_email(self):
        print("End of Email_Validation from forms.py")

        email=self.cleaned_data('email')
        print(email)
        print(type(email))
        if len(email)==0:
            raise forms.ValidationError("Email cannot be empty")
        elif email.isdigit():
            raise forms.ValidationError("Email should not contain only numbers")
        elif email[0].isdigit():
            raise forms.ValidationError("Email should not start with a number")
        return email