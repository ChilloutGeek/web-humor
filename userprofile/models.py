from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    datecreated = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=250, default='')

    def __str__(self):
        return self.name
