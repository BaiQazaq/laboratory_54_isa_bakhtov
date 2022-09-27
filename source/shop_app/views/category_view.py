from django.shortcuts import render, get_object_or_404
from shop_app.models import Category


def category_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'category.html', context={'category': category})