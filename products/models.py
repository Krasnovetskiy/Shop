from os import path

from django.db import models

from project.constants import max_digits, decimal_places
from project.mixins.models import PKMixin


def products_image(instance, filename):
    _name, extension = path.splitext(filename)
    return f'products/images/{str(instance.pk)}{extension}'


class Category(PKMixin):
    name = models.CharField(max_length=255)
    description = models.TextField(
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to=products_image,
        null=True
    )


class Product(PKMixin):
    name = models.CharField(max_length=255)
    description = models.TextField(
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to=products_image,
        null=True
    )
    sku = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category, blank=True)
    products = models.ManyToManyField('products.Product', blank=True)
    price = models.DecimalField(
        max_digits=max_digits,
        decimal_places=decimal_places)


# class Order(models.Model):
#    order_number = models.PositiveIntegerField(max_length=255)
#    is_paid = models.BooleanField(default=False)
#    is_active = models.BooleanField(default=True)
    # user = models.ForeignKey()
