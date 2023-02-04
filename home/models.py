from django.db import models

# Create your models here.
class Member(models.Model):
    user_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm = models.CharField(max_length=255)


class sell_your_car(models.Model):
     username = models.CharField(max_length=255)
     mobile = models.CharField(max_length=255)
    