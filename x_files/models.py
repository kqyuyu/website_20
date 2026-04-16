from django.db import models


class Episode(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    original_title = models.CharField(max_length=200, blank=True, verbose_name='Оригинальное название')
    season = models.PositiveSmallIntegerField(verbose_name='Сезон')
    episode_number = models.PositiveSmallIntegerField(verbose_name='Номер серии')
    air_date = models.DateField(verbose_name='Дата выхода')
    short_description = models.TextField(verbose_name='Краткое описание', blank=True)
    description = models.TextField(verbose_name='Полное описание', blank=True)
    director = models.CharField(max_length=100, blank=True)
    writer = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['season', 'episode_number']
        verbose_name = 'Эпизод'
        verbose_name_plural = 'Эпизоды'

    def __str__(self):
        return f'{self.season}x{self.episode_number:02d} — {self.title}'
