from django.db import models
from datetime import *
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    alias = models.SlugField(verbose_name='Alias категории')
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    def __str__(self):
        return 'Категория %s' % self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название подкатегории')
    alias = models.SlugField(verbose_name='Alias подкатегории')
    category = models.ForeignKey(Category)
    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
    def __str__(self):
        return 'Подкатегория %s' % self.name

class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название товара') # verbose_name как товар будет отображаться в админке
    price = models.IntegerField(default=0, verbose_name='Цена')
    alias = models.SlugField(verbose_name='Alias товара')

    category = models.ForeignKey(Category)
    #brend = models.ForeignKey(Brend, null=True)
    subcategory = models.ForeignKey(Subcategory)


    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
#

    def __str__(self):
        return 'Товар %s' % self.name

class Zakaz(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя официанта')
    place = models.CharField(max_length=255, verbose_name='Место')
    zakaz = models.CharField(max_length=255, verbose_name='Что заказал')
    summa = models.IntegerField(default=0, verbose_name='Сумма заказа')
    data = models.DateTimeField(default=timezone.now, verbose_name='Дата заказа')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ на %s' % self.summa


# Create your models here.
