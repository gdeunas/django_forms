from django.db import models


class Record(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.CharField(max_length=150, verbose_name='Содержимое')
    image = models.ImageField(upload_to='photos/', null=True, verbose_name='Превью (изображение)')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(verbose_name='Признак публикации')  # признак публикации (булевое поле)
    number_of_views = models.IntegerField(null=True, verbose_name='Количество просмотров', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
