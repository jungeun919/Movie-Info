from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', home, name = 'home'),
    path('create', create, name = 'create'),
    path('edit/<int:id>', edit, name = 'edit'),
    path('delete/<int:id>', delete, name = 'delete'),
]
