from django import forms
from django.contrib.auth.models import User
from .models import Customer

class UserSignup(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username '}),required=True,max_length=15)
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email '}),required=True,max_length=50)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name! '}),required=True,max_length=15)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter surname ! '}),required=True,max_length=15)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Secret word! '}),required=True,max_length=15)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Re-enter Secret word! '}),required=True,max_length=15)

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password']

class UserSignin(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username '}),required=True,max_length=15)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Secret word! '}),required=True,max_length=15)



class Stockform(forms.Form):
    companies_invested = forms.CharField(widget = forms.TextInput(attrs={'class': 'input', 'placeholder': 'Stocks', 'autocomplete': 'off'}))

