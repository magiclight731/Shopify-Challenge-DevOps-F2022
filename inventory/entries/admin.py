from django.contrib import admin

# Register your models here.
from .models import Warehouse, Item
admin.site.register(Warehouse)
admin.site.register(Item)
