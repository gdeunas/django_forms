from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')  # наименование
    description = models.CharField(max_length=150, verbose_name='Описание')  # описание

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')  # наименование
    description = models.CharField(max_length=150, verbose_name='Описание')  # описание
    image = models.ImageField(upload_to='photos/', verbose_name='Фотография')  # изображение
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category',
                                 verbose_name='Категория')  # категория
    price = models.FloatField(help_text='Введите цену за покупку', verbose_name='Цена за покупку')  # цена за покупку
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')  # дата создания
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='Дата последнего изменения')  # дата последнего изменения

    def __str__(self):
        return f'{self.name} {self.category}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
