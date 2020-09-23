from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from boards.models import Board
from boards.serializers import BoardSerializer
from categories.serializer import CategorySerializer


class ListView(ListAPIView):
    queryset = Board.objects.all()
    permission_classes = []
    serializer_class = BoardSerializer


class CreateView(CreateAPIView):
    queryset = Board.objects.all()
    permission_classes = []
    serializer_class = BoardSerializer


class RetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    lookup_url_kwarg = 'board_id'


class ListByCategoryView(ListAPIView):
    permission_classes = []
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(name_icontains=self.request.query_params.get('search', ''))
