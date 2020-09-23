from django.urls import path
from boards.views import ListByCategoryView, ListView, CreateView, RetrieveUpdateDestroyView

urlpatterns = [
    path('', ListView.as_view()),
    path('new/', CreateView.as_view()),
    path('category/<int:category_id>/', ListByCategoryView.as_view()),
    path('<int:board_id>/', RetrieveUpdateDestroyView.as_view()),
]
