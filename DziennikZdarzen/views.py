from django.contrib.auth import login, authenticate
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('changeLog:changeLog')
    else:
        form = UserCreationForm()
    return render(request, 'DziennikZdarzen/signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('changeLog:changeLog')
        else:
            return redirect('signup')
    else:
        form = AuthenticationForm()
    return render(request, 'DziennikZdarzen/signin.html', {'form': form})


def signout(request):
    return logout_then_login(request)


