from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class pizza(models.Model):
    type =  models.CharField(max_length=30)
    upsize = models.BooleanField() #Big or Small
    pizzaDetails = models.CharField(max_length=10) #Cheese, 1,2,or 3 toppings, special
    price = models.DecimalField(max_digits=4, decimal_places=2)

class sub(models.Model):
    type = models.CharField(max_length=30)
    upsize = models.BooleanField()
    price = models.DecimalField(max_digits=4, decimal_places=2)

class pasta(models.Model):
    type = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=4, decimal_places=2)

class salads(models.Model):
    type = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=4, decimal_places=2)

class dinnerPlatters(models.Model):
    type = models.CharField(max_length=30)
    upsize = models.BooleanField()
    price = models.DecimalField(max_digits=4, decimal_places=2)

class toppings(models.Model):
    type = models.CharField(max_length=30)
    
