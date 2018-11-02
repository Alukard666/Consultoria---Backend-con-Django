from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('clientes', views.ClienteList.as_view()),
    path('clientes/<int:pk>', views.ClienteDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]
