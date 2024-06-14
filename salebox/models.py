from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=88, null=False)
    product_img = models.ImageField(upload_to="salebox/pictures", null=False)
    is_available = models.BooleanField(null=False)
    description = models.CharField(max_length=300, null=False)
    price = models.IntegerField(null=False)

    def __str__(self):
        return f"{self.product_name}, {self.product_img},{self.is_available}, {self.description}, {self.price}"


class MixBox(models.Model):
    box_name = models.CharField(max_length=88, null=False)# tipo kak box for auto or for home
    included_in_the_box = models.ForeignKey(Product, on_delete=models.CASCADE)
    images = models.ImageField(upload_to="salebox/images", null=False)
    is_available = models.BooleanField(null=False)
    description_box = models.CharField(max_length=300, null=False)
    box_price = models.IntegerField(null=False)

    def __str__(self):
        return f"{self.box_name}, {self.included_in_the_box}, {self.images}, {self.is_available}, {self.description_box}, {self.box_price}"


# class Catigories(models.Model):
#     product_name = models.CharField(max_length=88, null=False)
#
#     class Meta:

