from django.db import models

# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название языка')
    code = models.CharField(max_length=10, unique=True, verbose_name='Код языка')
    flag = models.CharField(max_length=10, blank=True, verbose_name='Флаг')
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    sort = models.PositiveIntegerField(default=0, verbose_name='Сортировка')

    class Meta:
        ordering = ['sort', 'name']
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'

    def __str__(self):
        return f'{self.flag} {self.name}'