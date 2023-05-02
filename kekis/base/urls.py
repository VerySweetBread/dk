from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('project/<str:pk>/', views.project, name="project"),
    path('kvantum/', views.kvantum, name="kvantum"),
    path('account/<str:pk>/', views.account, name="account_home"),
    path('login/', views.login, name="login"),
    path('shop/', views.shop, name="shop"),
]