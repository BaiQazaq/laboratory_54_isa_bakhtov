from django.shortcuts import render, get_object_or_404
from shop_app.models import Good


def detail_view(request, pk):
    task = get_object_or_404(Good, pk=pk)
    return render(request, 'task.html', context={'task': task})