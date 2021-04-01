from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def showHomeView(request):
    return render(request, 'pages/home.html')
def showMenuView(request):
    return render(request, 'pages/menu.html')
def showShopView(request):
    return render(request, 'pages/shop.html')
def showNewsView(request):
    return render(request, 'pages/news.html')
def showSigninView(request):
    return render(request, 'pages/signin.html')

