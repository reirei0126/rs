from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    username = models.CharField('UserName', max_length=100)
    password1 = models.CharField('password1', max_length=100)
    password2 = models.CharField('password2', max_length=100)
    created_at = models.DateTimeField('作成日',default=timezone.now)

    def __str__(self):
        return self.username
