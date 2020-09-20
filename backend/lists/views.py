from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIVIew, ListCreateAPIView, RetrieveDestroyAPIView
from lists.models import List
from lists.serializers import ListSerializer
from categories.serializer import CategorySerializer


class ListCreateView(ListCreateAPIView):
    permission_classes = []
    queryset = List.objects.all()
    serializer_class = ListSerializer


class RetrieveDestroyView(RetrieveDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    lookup_url_kwarg = 'list_id'


class ListByCategoryView(ListAPIVIew):
    permission_classes = []
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(name_icontains=self.request.query_params.get('search', ''))
