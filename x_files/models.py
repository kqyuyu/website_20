from django.db import models


class Episode(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    original_title = models.CharField(max_length=200, blank=True, verbose_name='Оригинальное название')
    season = models.PositiveSmallIntegerField(verbose_name='Сезон')
    episode_number = models.PositiveSmallIntegerField(verbose_name='Номер серии')
    air_date = models.DateField(verbose_name='Дата выхода')
    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True, verbose_name='Рейтинг IMDb (0–10)')
    short_description = models.TextField(verbose_name='Краткое описание', blank=True)
    description = models.TextField(verbose_name='Полное описание', blank=True)
    director = models.CharField(max_length=100, blank=True)
    writer = models.CharField(max_length=100, blank=True)
    is_featured = models.BooleanField(default=False, verbose_name='Показывать на главной')

    class Meta:
        ordering = ['season', 'episode_number']
        verbose_name = 'Эпизод'
        verbose_name_plural = 'Эпизоды'

    def __str__(self):
        return f'{self.season}x{self.episode_number:02d} — {self.title}'
