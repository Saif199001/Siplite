from django.urls import path
from .views import product_list, wholesale_view, category_products, wholesale_category_products, product_detail

urlpatterns = [
    path('', product_list, name='product_list'),
    path('category/<slug:category_slug>/', product_list, name='category_products'),
    path('category/<slug:slug>/', category_products, name='category'),
    path('product/<slug:slug>/', product_detail, name='product_detail'),
     path('wholesale/<slug:category_slug>/', wholesale_category_products, name='wholesale_category'),
    path('wholesale/', wholesale_view, name='wholesale'),
]