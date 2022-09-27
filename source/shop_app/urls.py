from django.urls import path

from shop_app.views.products_view import products_view
from shop_app.views.product_view import product_view
from shop_app.views.product_add import product_add_view
from shop_app.views.category_add import category_add_view
from shop_app.views.category_view import category_view
from shop_app.views.categories_view import categories_view


urlpatterns = [
    path("", products_view, name='goods_page'),
    path("products/", products_view, name='goods_page'),
    path("products/<int:pk>", product_view, name='page_show_good'),
    path("products/add/", product_add_view, name='page_add_good'),
    path("categories/add/", category_add_view, name='page_add_category'),
    path("categories/<int:pk>", category_view, name='page_show_category'),
    path("categories/", categories_view, name='categories_page'),
]