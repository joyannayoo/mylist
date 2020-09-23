from django.urls import path
from categories.views import ListView, CreateView

urlpatterns = [
    path('', ListView.as_view()),
    path('new/', CreateView.as_view())
]