from django.db import models


# Create your models here.

class Event(models.Model):
    event_text = models.CharField(max_length= 5000)
    publication_date = models.DateTimeField('publication date', auto_now_add=True)



