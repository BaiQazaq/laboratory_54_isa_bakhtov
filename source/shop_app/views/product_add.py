from multiprocessing import context
from django.shortcuts import render, redirect
from shop_app.models import Good
from shop_app.models import Category


def product_add_view(request):
    if request.method == "GET":
        context = {
            'categories': Category.objects.all()
        }
        return render(request, 'create_product.html', context)
    print("++++"*5, request.POST.get('category'))
    good_data = {
        'title': request.POST.get('title'),
        'description': request.POST.get('description'),
        'price': request.POST.get('price'),
        'photo': request.POST.get('photo'),
    }
    category = Category.objects.get(title=request.POST.get('category'))
    good = Good.objects.create(**good_data, category=category)
    return redirect('page_show_good', pk=good.pk)
