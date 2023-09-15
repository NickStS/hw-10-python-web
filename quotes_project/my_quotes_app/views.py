from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm, UserLoginForm, AuthorForm, QuoteForm
from .models import Author, Quote

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            return redirect('author_detail', author_id=author.id)
    else:
        form = AuthorForm()
    
    return render(request, 'my_quotes_app/add_author.html', {'form': form})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.author = form.cleaned_data['author']
            quote.save()
            return redirect('quote_list')
    else:
        form = QuoteForm()
    
    return render(request, 'my_quotes_app/add_quote.html', {'form': form})

def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    quotes = Quote.objects.filter(author=author)
    return render(request, 'my_quotes_app/author_detail.html', {'author': author, 'quotes': quotes})

def quote_list(request):
    quotes = Quote.objects.all()
    return render(request, 'my_quotes_app/quote_list.html', {'quotes': quotes})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('quote_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('quote_list')
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})
