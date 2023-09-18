from django.db import models

class Places(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
 
# Create your models here.
