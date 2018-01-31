from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django import forms

from .models import Investment
from .forms import UserRegistrationForm


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form' : form})


def investments(request):
    investments = Investment.objects.all()
    return render(request, 'investments.html', {'investments': investments})


def write_investment_to_file(request, investment_id):
    investment_content = Investment.objects.filter(id=investment_id).values('start_date', 'end_date', 'title', 'description')
    with open('saved_investments/' + investment_id + '.txt', 'w') as f:
        f.write(str(investment_content))
    return render(request, 'save-investment.html')

def read_investment_from_file(request, investment_id):
    try:
        with open('saved_investments/' + investment_id + '.txt', 'r') as f:
            file_content = f.read()
            return render(request, 'read-investment.html', {'investment' : file_content})
    except FileNotFoundError:
        return render(request, 'read-investment.html', {'investment' : 'Oooops! I didn\'t find a file :('})
