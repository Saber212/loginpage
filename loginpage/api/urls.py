from django.contrib import admin
from django.urls import path,include
from .views import Users

urlpatterns = [
    path('list/', Users.as_view(), name='users')
]