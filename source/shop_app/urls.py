from django.urls import path

from shop_app.views.products_view import products_view
from shop_app.views.product_view import product_view
from shop_app.views.product_add import product_add_view
from shop_app.views.category_add import category_add_view

urlpatterns = [
    path("", products_view, name='base'),
    path("products/", products_view, name='base'),
    path("products/<int:pk>", product_view, name='show_good'),
    path("products/add/", product_add_view, name='add_good'),
    path("categories/add/", category_add_view, name='add_category'),
]