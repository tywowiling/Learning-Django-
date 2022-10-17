from django.db import models

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=255)
    password = models.TextField(max_length=255)

    def __str__(self):
        return "{}".format(self.username)