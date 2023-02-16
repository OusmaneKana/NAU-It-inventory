from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/transaction', views.index, name='transaction'),
]