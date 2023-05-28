from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Todo(models.Model):
    text_todo = models.CharField(max_length=200)
    date_start = models.DateTimeField('date_start')
    date_end = models.DateTimeField('date_end')

    def __str__(self):
        return self.text_todo
