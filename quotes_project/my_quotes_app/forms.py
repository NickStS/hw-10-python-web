from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Author, Quote 

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'birth_date', 'bio')
        
class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ('text', 'author')