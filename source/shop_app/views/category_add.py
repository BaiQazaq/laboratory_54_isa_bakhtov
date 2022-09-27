from django.shortcuts import render, redirect
from shop_app.models import Category


def category_add_view(request):
    if request.method == "GET":
        return render(request, 'create_category.html')
    category_data = {
        'title': request.POST.get('title'),
        'description': request.POST.get('description'),
    }
    category = Category.objects.create(**category_data)
    return redirect('page_add_category', pk=category.pk)
