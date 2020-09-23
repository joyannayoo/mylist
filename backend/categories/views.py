from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, CreateAPIView
from categories.models import Category
from categories.serializer import CategorySerializer


class ListView(ListAPIView):
    permission_classes = []
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CreateView(CreateAPIView):
    permission_classes = []
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
