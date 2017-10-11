from django.db import models
from datetime import *
from django.utils import timezone

class Category(models.Model):
    category_name = models.CharField(max_length=255, verbose_name='Название категории')
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    alias = models.SlugField(verbose_name='Alias категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return 'Категория %s' % self.category_name


class Item(models.Model):
    item_name = models.CharField(max_length=255,
                            verbose_name='Название товара')  # verbose_name как товар будет отображаться в админке
    price = models.IntegerField(default=0, verbose_name='Цена')
    alias = models.SlugField(verbose_name='Alias товара')
    category = models.ForeignKey(Category)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return 'Товар %s' % self.item_name

class OrderPlace(models.Model):
    place_name = models.CharField(max_length=255, null=True, verbose_name="Название ресторана")

    class Meta:
        verbose_name = 'Название ресторана'
        verbose_name_plural = 'Названия ресторанов'

    def __str__(self):
        return 'Ресторан %s' % self.place_name


class Waiters(models.Model):
    waiter_name = models.CharField(max_length=255, null=True, verbose_name="Имя официанта")
    work_place = models.ForeignKey(OrderPlace, null=True, verbose_name="Место работы")
    class Meta:
        verbose_name = 'Имя официанта'
        verbose_name_plural = 'Имена официантов'

    def __str__(self):
        return 'Официанта %s' % self.waiter_name


class Order(models.Model):
    waiter = models.ForeignKey(Waiters, null=True)
    order_place = models.ForeignKey(OrderPlace, null=True)
    date = models.DateTimeField(default=timezone.now, verbose_name='Дата заказа')
    items = models.ManyToManyField(Item, through='OrderLine')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ %s' % self.id


class OrderLine(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    count = models.IntegerField(default=0, null=True)
    item_price = models.IntegerField(default=0, null=True)

    class Meta:
        verbose_name = 'Строка заказа'
        verbose_name_plural = 'Строки заказа'

    def __str__(self):
        return 'Количество %s' % self.count

# Create your models here.
