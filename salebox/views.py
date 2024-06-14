import requests
from django.shortcuts import render

# from .forms import ProductForm, MixBoxForm
from django.views.generic import ListView

from .models import MixBox, Product


# Create your views here.

# def index(request):
#     return render(request, 'product_list.html')  # Создайте шаблон для вашей страницы
# class ProductList(ListView):
#     model = Product
#     extra_context = {
#         'title': 'List of products'}

class Product_list(ListView):
    model = Product
    template_name = 'salebox/product_list.html'
    context_object_name = 'product'
    paginate_by = 15


class MixBoxList(ListView):
    model = MixBox
    template_name = 'salebox/mix_box_list.html'
    context_object_name = 'mixbox'
    paginate_by = 15


# def index(request):
#     url = 'http://api.openweathermap.org/data/2.5/weather?appid=d03ae58a91ede824fd36ca37e7769f31&q=PRAGUE'
#     response = requests.get(url)
#     weather_data = response.json()
#
#     context = {
#         'temperature': weather_data['main']['temp'],
#         'description': weather_data['weather'][0]['description'],
#     }
#     return render(request, 'product_list.html', context)
