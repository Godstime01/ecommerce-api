from django.contrib import admin
from .models import Product, Category, Rating


admin.site.register([Category, Rating, Product])