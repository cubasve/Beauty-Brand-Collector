from django.contrib import admin
from .models import Brand, Purchase, Product

# Register your models here.

admin.site.register(Brand)
admin.site.register(Purchase)
admin.site.register(Product)