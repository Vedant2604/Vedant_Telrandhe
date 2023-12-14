from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index/', views.index, name="index"),   
    path('addContact/',views.addContact,name="addContact"),
    path('deleteContact/<int:id>/',views.deleteContact,name="deleteContact"),
    path('updateContact/<int:id>/',views.updateContact,name="updateContact"),
]