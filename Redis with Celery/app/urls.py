from django.urls import path
from app import views

urlpatterns = [
    path('timer', views.timer),
    path('write', views.write),
]
