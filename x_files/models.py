from django.db import models
from django.utils import timezone


class Episode(models.Model):
    """Модель эпизодов сериала «Секретные материалы» (The X-Files)."""

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

    @property
    def episode_display(self):
        """Форматированный номер серии: S01E02"""
        return f'S{self.season:02d}E{self.episode_number:02d}'


class News(models.Model):
    """Модель новостей о сериале «Секретные материалы»."""
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='URL', help_text='Автоматически формируется из заголовка')
    summary = models.TextField(max_length=500, verbose_name='Краткое содержание', help_text='Отображается на главной странице' )
    content = models.TextField(verbose_name='Полный текст новости')
    image = models.ImageField(upload_to='news_images/', blank=True, null=True, verbose_name='Изображение')
    author = models.CharField(max_length=100, default='Редакция', verbose_name='Автор')
    published_at = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации' )

    class Meta:
        ordering = ['-published_at']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', args=[self.slug])


class Character(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='characters/', blank=True, null=True)

    def __str__(self):
        return self.name