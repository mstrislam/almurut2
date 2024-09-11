from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render
from django.views import View
#from market.models import
class HomeView(TemplateView):
    template_name = 'index.html'

class F404View(TemplateView):
    template_name = '404.html'

class FaqView(TemplateView):
    template_name = 'faq.html'


class FavoritesView(TemplateView):
    template_name = 'favorites.html'

class LoginView(TemplateView):
    template_name = 'login.html'

class ProductDetailView(TemplateView):
    template_name = 'product-detail.html'

class ProductListView(TemplateView):
    template_name = 'product-list.html'

class RegisterView(TemplateView):
    template_name = 'register.html'

class ShoppingView(TemplateView):
    template_name = 'shopping-cart.html'


