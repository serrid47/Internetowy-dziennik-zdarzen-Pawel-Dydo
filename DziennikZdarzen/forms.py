from django.forms import ModelForm, Textarea
from django import forms
from django.contrib.auth.models import Permission
from django.contrib.auth.forms import UserCreationForm
from changeLog.models import MyUser


class RegistrationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('username',)

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.save()
        if commit:
            user.save()
        return user