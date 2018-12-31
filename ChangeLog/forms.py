from django import forms
from .models import ChangeLog, Log, UserInChangelog, MyUser
from django.core.files.images import get_image_dimensions


class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields =('log_text',)


class LogSearchForm(forms.Form):
    search_text = forms.CharField(label='search_text', max_length=5000)


class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=5000)
    password = forms.CharField(label='password', max_length=5000)


class CreateChangelogForm(forms.ModelForm):
    class Meta:
        model = ChangeLog
        fields =('nazwa',)


class InviteToChangelogForm(forms.Form):
    username = forms.CharField(label='username', max_length=5000)
    
    
class UserInChangelogForm(forms.ModelForm):
    class Meta:
        model = UserInChangelog
        fields = ('user', 'permission',)


class UserAvatarForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('first_name', 'last_name', 'mail', 'avatar', )





