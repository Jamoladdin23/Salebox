from django.urls import path
from . import views

urlpatterns = [
    path('', views.Product_list.as_view(), name='Product_list'),
    path('products/', views.MixBoxList.as_view(), name='box_list')

]