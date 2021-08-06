from django.db import models
from tinymce import models as tinymce_models


class Location(models.Model):
    title = models.CharField('Название локации', max_length=200)
    description_short = models.TextField('Краткое описание', blank=True)
    description_long = tinymce_models.HTMLField('Полное описание', blank=True)
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    class Meta:
        verbose_name_plural = 'Локации'
        verbose_name = 'Локация'
        ordering = ('title',)

    def __str__(self):
        return self.title[:15]


class Image(models.Model):
    image = models.ImageField('Изображение', upload_to='locations/')
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name='imgs',
        verbose_name='Локация'
        )
    order = models.PositiveIntegerField('Порядок', default=0, blank=True)

    class Meta:
        verbose_name_plural = 'Изображения'
        verbose_name = 'Изображение'
        ordering = ('order',)

    def __str__(self):
        return f'{self.id} {self.location.title}'
