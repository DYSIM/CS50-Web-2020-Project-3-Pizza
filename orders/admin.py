from django.contrib import admin
from orders.models import pizza, sub, pasta, salads, dinnerPlatters,toppings,order,sub_addition
# Register your models here.

admin.site.register(pizza)
admin.site.register(sub)
admin.site.register(sub_addition)
admin.site.register(pasta)
admin.site.register(salads)
admin.site.register(dinnerPlatters)
admin.site.register(toppings)
admin.site.register(order)
