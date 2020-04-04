from django.shortcuts import render, get_object_or_404
from . import models


def categories(request):
    categories = models.categories.objects.all()
    return render(request, 'Molavi/categories.html', {'categories': categories})


def raftare_manfi(request, question_id):
    raftare_manfi = get_object_or_404(models.categories, pk=question_id)
    return render(request, 'Molavi/raftare_manfi.html', {'raftare_manfi': raftare_manfi})


# def jameh(request, question_id):
#     jameh = get_object_or_404(models.categories, pk=question_id)
#     return render(request, 'Molavi/jameh.html', {'jameh': jameh})
