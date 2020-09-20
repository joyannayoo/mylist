from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView
from categories.models import Category
from categories.serializer import CategorySerializer

class ListCreateView(ListCreateAPIView):
    permission_classes = []
    queryset = Category.objects.all()
    serializer_class = CategorySerializer