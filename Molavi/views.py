from django.shortcuts import render, get_object_or_404
from . import models


def categories(request):
    categories = models.categories.objects.all()
    return render(request, 'Molavi/categories.html', {'categories': categories})


def all_details(request, question_id):
    categories_raftare_manfi = get_object_or_404(models.categories, pk=question_id)
    categories_raftare_mosbat = get_object_or_404(models.categories,pk=question_id)
    categories_jameh = get_object_or_404(models.categories,pk=question_id)
    return render(request, 'Molavi/raftare_manfi.html', {'categories_raftare_manfi': categories_raftare_manfi,
                                                         'categories_raftare_mosbat':categories_raftare_mosbat,
                                                         'categories_jameh' : categories_jameh,
                                                         })


def results(request,question_id):
   test = models.raftar_manfi.objects.filter(title='مقدمه ای بر رفتار منفی',pk=question_id)
   test2 = models.raftar_manfi.objects.filter(title='آزمندی',pk=question_id)
   test3 = models.raftar_manfi.objects.filter(title='بخل', pk=question_id)
   return render(request, 'Molavi/results.html', {'test':test,'test2':test2,'test3':test3})
