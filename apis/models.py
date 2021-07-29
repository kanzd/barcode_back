from django.db import models

# Create your models here.


class UserModel(models.Model):
    id=models.AutoField
    username=models.CharField(max_length=300)
    password=models.CharField(max_length=300)
    