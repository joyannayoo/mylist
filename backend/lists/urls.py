from django.urls import path
from lists.views import ListByCategoryView, ListCreateView, RetrieveDestroyView

urlpatterns = [
    path('', ListCreateView.as_view()),
    path('new/', ListCreateView.as_view()),
    path('category/<int:category_id>/', ListByCategoryView.as_view),
    path('<int:list_id>/', RetrieveDestroyView.as_view),
]
