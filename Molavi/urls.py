from django.urls import path
from . import views


app_name = 'Molavi'

urlpatterns = [
    #/categories/
    path('categories/', views.categories,name='categories'),
    #categories/id/
    path('categories/<int:question_id>/raftare_manfi/', views.raftare_manfi, name='raftare_manfi'),
    # path('categories/<int:question_id>/jameh/', views.jameh, name='jameh'),



]
