from django.urls import path
from . import views


app_name = 'Molavi'

urlpatterns = [
    #/categories/
    path('categories/', views.categories,name='categories'),
    #categories/id/
    path('categories/<int:question_id>/', views.all_details, name='all_details'),
    path('categories/<int:question_id>/results', views.results, name='results'),




]
