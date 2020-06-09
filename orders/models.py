from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.

class pizza(models.Model):
    Type =  models.CharField(max_length=30)
    Size = models.CharField(max_length=5) #Big or Small
    Details = models.CharField(max_length=10) #Cheese, 1,2,or 3 toppings, special
    Price = models.DecimalField(max_digits=4, decimal_places=2)

class sub(models.Model):
    Type = models.CharField(max_length=30)
    Size = models.CharField(max_length=5)
    Price = models.DecimalField(max_digits=4, decimal_places=2)

class sub_addition(models.Model): #for steak + {cheese, mushroom, green pepper, onions} Combinations
    Type = models.CharField(max_length=20)
    Size = models.CharField(max_length=5, blank=True, default='')
    AdditionalPrice = models.DecimalField(max_digits=4, decimal_places=2)

class pasta(models.Model):
    Type = models.CharField(max_length=30)
    Price = models.DecimalField(max_digits=4, decimal_places=2)

class salads(models.Model):
    Type = models.CharField(max_length=30)
    Price = models.DecimalField(max_digits=4, decimal_places=2)

class dinnerPlatters(models.Model):
    Type = models.CharField(max_length=30)
    Size = models.CharField(max_length=5)
    Price = models.DecimalField(max_digits=4, decimal_places=2)

class toppings(models.Model):
    Type = models.CharField(max_length=30)

class order(models.Model):
    Name = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content_type =   models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object=GenericForeignKey('content_type', 'object_id')
    Topping_1 = models.ForeignKey(toppings, blank=True, null=True, on_delete=models.CASCADE, related_name = "Topping_1")
    Topping_2 = models.ForeignKey(toppings, blank=True, null=True, on_delete=models.CASCADE, related_name = "Topping_2")
    Topping_3 = models.ForeignKey(toppings, blank=True, null=True, on_delete=models.CASCADE, related_name = "Topping_3")
    Sub_1 = models.ForeignKey(sub_addition, blank=True, null=True, on_delete=models.CASCADE, related_name = "Sub_1")
    Sub_2 = models.ForeignKey(sub_addition, blank=True, null=True, on_delete=models.CASCADE, related_name = "Sub_2")
    Sub_3 = models.ForeignKey(sub_addition, blank=True, null=True, on_delete=models.CASCADE, related_name = "Sub_3")
    Sub_4 = models.ForeignKey(sub_addition, blank=True, null=True, on_delete=models.CASCADE, related_name = "Sub_4")
