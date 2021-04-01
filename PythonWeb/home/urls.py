from django.urls import path
from . import views

urlpatterns = [
    path('', views.showHomeView),
    path('home/', views.showHomeView),
    path('menu/', views.showMenuView),
    path('shop/', views.showShopView),
    path('news/', views.showNewsView),
    path('signin/', views.showSigninView),
]