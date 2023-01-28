from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles_list, name='articles_list'),
    path('feeds/', views.feeds_list, name='feeds_list'), 
    path('contact-us/', views.contactus, name='contact_us'), 
    path('privacy-policy/', views.privacypolicy, name='privacy_policy'), 




]