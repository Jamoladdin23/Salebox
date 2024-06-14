from django import forms
from .models import Product, MixBox


def validate_name(value):
    if value[0].isdigit():
        raise forms.ValidationError("The product name cannot contain a number")

class ProductForm(forms.Form):
    product_name = forms.CharField(max_length=88)  # tipo kak box for auto or for home
    Product_img = forms.ImageField
    is_available = forms.BooleanField()
    description = forms.CharField(max_length=300)
    price = forms.IntegerField(null=False)


class MixBoxForm(forms.Form):
    box_name = forms.CharField(max_length=88, null=False)
    included_in_the_box =  forms.ModelChoiceField(queryset=Product.objects.all())
    images = forms.ImageField
    is_available = forms.BooleanField()
    description_box = forms.CharField(max_length=300, null=False)
    box_price = forms.IntegerField(null=False)


