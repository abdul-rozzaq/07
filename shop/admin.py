from django.contrib import admin

# Register your models here.
from .models import Phone, Category



admin.site.register(Phone)
admin.site.register(Category)