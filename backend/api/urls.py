from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.list_user),
    path('users/create', views.create_user)
]
