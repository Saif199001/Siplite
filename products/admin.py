from django.contrib import admin
from .models import Product, Category, WholesaleCategory, WholesaleProduct



# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(WholesaleCategory)
admin.site.register(WholesaleProduct)

