from django.contrib.auth import login, authenticate
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.urls import views as auth_views
from .forms import RegistrationForm
from django.contrib.auth import logout
from django.contrib.auth import get_user_model

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    else:
        form = RegistrationForm()
    return render(request, 'DziennikZdarzen/signup.html', {'form': form})

class LoginUserView(auth_views.LoginView):
    template_name = 'DziennikZdarzen/signin.html'



def signout(request):
    return logout_then_login(request)


