from django.urls import path
from categories.views import ListCreateView

urlpatterns = [
    path('list', ListCreateView.as_view())
]