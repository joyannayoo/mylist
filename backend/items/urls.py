from django.urls import path
from items.views import ListCreateView, RetrieveDestroyView

urlpatterns = [
    path('', ListCreateView.as_view()),
    path('new/', ListCreateView.as_view()),
    path('<int:item_id>/', RetrieveDestroyView.as_view),
]
