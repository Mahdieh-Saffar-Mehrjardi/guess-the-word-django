from django.db import models
# Create your models here.


class Word(models.Model):
    name = models.CharField(max_length=32, verbose_name='نام')

    class Meta:
        verbose_name = 'کلمه'
        verbose_name_plural = 'کلمه‌ها'

    def __str__(self):
        return self.name