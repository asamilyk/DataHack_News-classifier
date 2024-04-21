from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_cats_tags/', views.get_cats_tags, name='get_cats_tags'),
    path('get_tags/', views.get_tags, name='get_tags'),
    path('get_category/', views.get_category, name='get_category'),
    path('get_picture/', views.get_picture, name='get_picture')
]