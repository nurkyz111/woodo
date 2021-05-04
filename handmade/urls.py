from django.contrib import admin
from django.urls import path
from .views import main, products, contact, about, company, search, category_detail, product_detail



urlpatterns = [
    path('', main, name='main'),
    path('products/', products, name='products'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('company/', company, name='company'),
    path('search/', search, name='search'),
    path('category/<int:id>', category_detail, name='category_detail'),
    path('product/<int:id>', product_detail, name='product_detail'),
]