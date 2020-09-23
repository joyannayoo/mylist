from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from items.models import Item
from items.serializers import ItemSerializer


class ListCreateView(ListCreateAPIView):
    permission_classes = []
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        return Item.objects.filter(name__icontains=self.request.query_params.get('search', ''))


class RetrieveDestroyView(RetrieveDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_url_kwarg = 'item_id'
