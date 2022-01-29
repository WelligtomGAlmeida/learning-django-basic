from django.db import models


class Product(models.Model):
    name = models.CharField('Name', max_length=100)
    price = models.DecimalField('Price', decimal_places=2, max_digits=8)
    stock = models.IntegerField('Units in Stock')


class Customer(models.Model):
    name = models.CharField('Name', max_length=100)
    lastName = models.CharField('Last Name', max_length=100)
    email = models.EmailField('E-mail', max_length=100)