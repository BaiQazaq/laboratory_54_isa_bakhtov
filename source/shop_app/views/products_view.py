from django.shortcuts import render
from shop_app.models import Good

def base_view(request):
    tasks = Good.objects.all()
    context = {
        "tasks": tasks
    }
    return render(request, 'base.html', context)