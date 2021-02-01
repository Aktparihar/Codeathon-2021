from django.urls import path
from .views import index,Register_view,Login_view

urlpatterns = [
    path('', index),
    path('register/', Register_view),
    path('login/', Login_view),
]