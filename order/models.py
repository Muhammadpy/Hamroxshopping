from itertools import product
from unicodedata import name
from django.db import models

from main.models import Product

# Create your models here.
class COUNTRIES(models.TextChoices):
    uzb = "uzbekistan ", "uzbekistan"
    kg = "kirgistan", "kirgistan"
    rus = "rus",    "rus"


class OrderStatus(models.IntegerChoices):
    created = (1, "created")
    on_process = (2, "on_process")
    fineshed = (3, "fineshed")
    cencelled = (0,  "cencelled")

class Order (models.Model):
    first_name = models.CharField('Ismi', max_length=22)
    surname = models.CharField('Familiya', max_length=22)
    email = models.EmailField('email', max_length=45)
    phone = models.CharField('phone', max_length=13)
    adress_1 = models.CharField('adress_1', max_length=99)
    adress_2 = models.CharField('adress_1', max_length=99  , blank=True )
    country = models.CharField('davlat', max_length=99  , choices = COUNTRIES.choices )
    city = models.CharField('kocha', max_length=99  )
    street = models.CharField('kocha', max_length=99  )
    zip_code = models.PositiveIntegerField('POCHTAINDEKSI')
    status = models.CharField('Buyurtma holati', max_length=99  , choices=OrderStatus.choices,)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)
    total_price = models.PositiveIntegerField(default=0)


        
