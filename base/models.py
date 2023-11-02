from django.db import models
from datetime import datetime
from django.contrib.auth.models import User




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    email = models.EmailField()
    job = models.CharField(max_length=200)
    description = models.CharField(max_length=2550000)
    phonenumber = models.CharField(max_length=15)
    datecreated = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering = ['-datecreated']

    def __str__(self):
        return self.user.username