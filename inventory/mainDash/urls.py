from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('assigne_retrieve/', views.assigne_retrive, name="assigne_retrieve"),
    path('add_device/', views.add_device, name="add_device")
]