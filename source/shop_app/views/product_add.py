from django.shortcuts import render, redirect
from shop_app.models import Good


def product_add_view(request):
    if request.method == "GET":
        return render(request, 'create_task.html')
    task_data = {
        'title': request.POST.get('title'),
        'description': request.POST.get('description'),
        'category': request.POST.get('category'),
        'price': request.Post.get('price'),
        'photo': request.Post.get('photo')
    }
    task = Good.objects.create(**task_data)
    return redirect('show', pk=task.pk)
