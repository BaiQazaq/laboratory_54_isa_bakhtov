from django.shortcuts import render
from shop_app.models import Good

def products_view(request):
    tasks = Good.objects.all()
    context = {
        "tasks": tasks
    }
    return render(request, 'base.html', context)