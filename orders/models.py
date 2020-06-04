from django.db import models

# Create your models here.

class pizza(models.Model):
    type =  models.CharField(max_length=20) #Pizza or Sub or Pasta  or Salad or Dinner Platter?
    upsize = models.BooleanField() #Big or Small
    pizzaDetails = models.CharField(max_length=10) #Cheese, 1,2,or 3 toppings, special
    price = models.DecimalField(max_digits=4, decimal_places=2)
