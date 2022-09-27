from unicodedata import category
from django.shortcuts import render
from shop_app.models import Category

def categories_view(request):
    categories = Category.objects.all()
    context = {
        "categories": categories
    }
    return render(request, 'categories.html', context)