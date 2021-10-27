from django.db import models
from django.db.models.base import Model

# Create your models here.
class logpage(models.Model):
    username=models.CharField(max_length=200)
    email=models.CharField(max_length=150)
    password=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    class Mete:
        db_table="reg"