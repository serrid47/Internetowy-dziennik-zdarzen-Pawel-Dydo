from django import forms


class LogForm(forms.Form):
    log_text = forms.CharField(label='Log Text', max_length=5000)


class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=5000)
    password = forms.CharField(label='password', max_length=5000)