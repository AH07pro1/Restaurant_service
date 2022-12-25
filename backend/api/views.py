from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from .models import User
from .serializer import UserSerializer
# Create your views here.

class ListUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

list_user = ListUsers.as_view()

class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

create_user = CreateUser.as_view()