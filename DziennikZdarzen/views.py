from django.contrib.auth.views import logout_then_login
from changeLog.models import MyUser
from changeLog.forms import UserAvatarForm
from django.shortcuts import render, redirect
from django.contrib.auth.urls import views as auth_views
from .forms import RegistrationForm
from django.views.generic import View

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


class userprofile(View):
    template_name = 'DziennikZdarzen/profile.html'

    def get(self, request, name):
        profile = MyUser.objects.get(username=name)
        context = {'profile': profile}
        return render(request, 'DziennikZdarzen/profile.html', context)


class yourprofile(View):
    template_name = 'DziennikZdarzen/yourprofile.html'

    def post(self,request):
        profile = MyUser.objects.get(username=request.user.username)
        form = UserAvatarForm(request.POST, request.FILES)
        if form.is_valid():
            profile.avatar = form.cleaned_data['avatar']
            profile.save()
        context = {'profile': profile, 'form': form}
        return render(request, 'DziennikZdarzen/yourprofile.html', context)


    def get(self, request):
        profile = MyUser.objects.get(username=request.user.username)
        form = UserAvatarForm()
        context = {'profile': profile, 'form': form}
        return render(request, 'DziennikZdarzen/yourprofile.html', context)




