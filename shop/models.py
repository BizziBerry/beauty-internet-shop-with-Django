from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название товара'
    )
    description = models.TextField(
        verbose_name='Описание товара'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена товара'
    )
    image = models.ImageField(
        upload_to='products/',
        verbose_name='Изображение товара',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='Дата создания'
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at']

    def __str__(self):
        return self.name