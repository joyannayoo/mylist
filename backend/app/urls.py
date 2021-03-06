"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework_simplejwt import views as jwt_views
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', jwt_views.TokenObtainPairView.as_view()),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view()),
    path('api/token/verify/', jwt_views.TokenVerifyView.as_view()),
    path('api/users/', include('users.urls')),
    path('api/categories/', include('categories.urls')),
    path('api/boards/', include('boards.urls')),
    path('api/items/', include('items.urls')),
]

urlpatterns.append(path('api/docs/', include_docs_urls(
    title='Django Template', schema_url='/', permission_classes=[])))
