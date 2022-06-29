from django.shortcuts import render
from rest_framework import viewsets
from .models import Link 
from .serializers import Linkserializer
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import DestroyAPIView

# Create your views here.

class PostListApi(ListAPIView):
     queryset = Link.objects.filter(active=True)
     serializer_class = Linkserializer 

class PostCreateApi(CreateAPIView):
     queryset = Link.objects.filter(active=True)
     serializer_class = Linkserializer

class PostDetailApi(RetrieveAPIView):
     queryset = Link.objects.filter(active=True)
     serializer_class = Linkserializer

class PostUpdateApi(UpdateAPIView):
     queryset = Link.objects.filter(active=True)
     serializer_class = Linkserializer 

class PostDeleteApi(DestroyAPIView):
     queryset = Link.objects.filter(active=True)
     serializer_class = Linkserializer 
