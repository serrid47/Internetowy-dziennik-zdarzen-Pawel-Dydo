from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
   pass


class Log(models.Model):
    log_text = models.CharField(max_length= 5000)
    publication_date = models.DateTimeField('publication date', auto_now_add=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)






