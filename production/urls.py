
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('', views.index , name="home"),
    path('products_list',views.list_products, name='list_products'),
    path('about',views.about, name='about'),

    
    path('product_details/<pk>',views.detail_product,name='detail_product')
]
