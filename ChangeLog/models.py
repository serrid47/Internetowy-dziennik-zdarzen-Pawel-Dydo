from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

import changeLog

PERMISSIONS = (
    ('d', 'D'),
    ('r', 'R'),
    ('rw', 'RW'),
    ('rwx', 'RWX'),
    ('rwi', 'RWI'),
    ('rwxi', 'RWXI'),
    ('rwxia', 'RWXIA'),
)


class MyUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', default='avatars/none/no-img.jpg')
    mail = models.EmailField(max_length=250)


class ChangeLog(models.Model):
    nazwa = models.CharField(max_length=250)


class UserInChangelog(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    changeLog = models.ForeignKey(ChangeLog, on_delete=models.CASCADE)
    permission = models.CharField(max_length=200, choices=PERMISSIONS, default='rw')

    @classmethod
    def create(self, user, changelog):
        user_in = self(user=user)
        user_in = self(changeLog=changelog)
        return user_in


class Log(models.Model):
    log_text = models.CharField(max_length=5000)
    publication_date = models.DateTimeField('publication date', auto_now_add=True)
    user_changelog = models.ForeignKey(UserInChangelog, on_delete=models.CASCADE)











