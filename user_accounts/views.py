from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm

def get_started(request):
    return render(request, 'user_accounts/get_started.html')


def register(request):
    form = CreateUserForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect('user_accounts:login')

    ctx = {
        'form': form,
    }

    return render(request, 'user_accounts/register.html', ctx)


def login_(request):
    form = AuthenticationForm(request.POST or None)

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog_post:article_list')

    ctx = {
        'form': form,
    }

    return render(request, 'user_accounts/login.html', ctx)

@login_required(redirect_field_name='user_accounts:login')
def logout_(request):
    logout(request)
    return redirect('user_accounts:get_started')