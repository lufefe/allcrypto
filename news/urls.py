from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles_list, name='articles_list'),
    path('feeds/', views.feeds_list, name='feeds_list'), #TODO -> create a list view of all news article


]