from django.urls import path
from . import views

urlpatterns = [
    path('<str:pk>/', views.main, name="account_home"),

]