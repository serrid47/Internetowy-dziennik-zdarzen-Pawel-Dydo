from django import forms
from .models import ChangeLog, Log


class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields =('log_text',)


class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=5000)
    password = forms.CharField(label='password', max_length=5000)


class CreateChangelogForm(forms.ModelForm):
    class Meta:
        model = ChangeLog
        fields =('nazwa',)
