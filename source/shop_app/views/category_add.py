from django.shortcuts import render, redirect
from shop_app.models import Category


def add_view(request):
    if request.method == "GET":
        return render(request, 'create_task.html')
    task_data = {
        'title': request.POST.get('title'),
        'description': request.POST.get('description'),
    }
    task = Category.objects.create(**task_data)
    return redirect('show', pk=task.pk)
