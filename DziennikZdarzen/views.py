from django.contrib.auth.views import logout_then_login
from changeLog.models import MyUser
from changeLog.forms import UserAvatarForm
from django.shortcuts import render, redirect
from django.contrib.auth.urls import views as auth_views
from .forms import RegistrationForm
from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin


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


class userprofile(LoginRequiredMixin, View):
    model = MyUser
    fields = ['first_name', 'last_name', 'avatar']

    def get(self, request, name):
        profile = MyUser.objects.get(username=name)
        context = {'profile': profile}
        return render(request, 'DziennikZdarzen/profile.html', context)


class yourprofile(LoginRequiredMixin, View):
    def post(self, request):
        profile = MyUser.objects.get(username=request.user.username)
        form = UserAvatarForm(request.POST, request.FILES)
        if form.is_valid():
            if (form.cleaned_data['avatar'] != 'avatars/none/no-img.jpg'):
                profile.avatar = form.cleaned_data['avatar']
            profile.first_name = form.cleaned_data['first_name']
            profile.last_name = form.cleaned_data['last_name']
            profile.mail = form.cleaned_data['mail']
            profile.save()
        context = {'profile': profile, 'form': form}
        return render(request, 'DziennikZdarzen/yourprofile.html', context)

    def get(self, request):
        profile = MyUser.objects.get(username=request.user.username)
        form = UserAvatarForm(initial={'first_name': profile.first_name, 'last_name': profile.last_name,
                                       'mail': profile.mail, 'avatar': profile.avatar.url})
        context = {'profile': profile, 'form': form}
        return render(request, 'DziennikZdarzen/yourprofile.html', context)
