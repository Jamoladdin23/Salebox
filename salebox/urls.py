from django.urls import path
from . import views

urlpatterns = [
    path('', views.MixBoxList.as_view(), name='box_list'),
    path('products/<int:pk>', views.ProductList.as_view(), name='prod'),

]
