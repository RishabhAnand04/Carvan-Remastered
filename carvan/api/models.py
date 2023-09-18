from django.db import models

class Places(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    rating = models.IntegerField(null=True)
    imgage = models.ImageField(null=True)
    description = models.CharField(max_length=200)

class Visiting(models.Model):
    name = models.CharField(max_length=200)
    city = models.ForeignKey(Places, max_length=200, on_delete = models.PROTECT)
    imgage = models.ImageField(null=True)
    rating = models.IntegerField(null=True)
    visits_per_month = models.IntegerField(null=True)
    ticket_price = models.IntegerField(null=True)
    hours_open = models.IntegerField(null=True)
    accessibility_range = models.IntegerField(null=True)
    location = models.CharField(max_length=200)
    highlight = models.CharField(max_length=200)
    family_friendly = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

