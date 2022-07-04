from distutils.command.upload import upload
from django.db import models
from django.forms import CharField

# Create your models here.

class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    desc = models.TextField()
    
    