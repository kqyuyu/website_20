from django.contrib import admin
from .models import Episode

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('episode_display', 'title', 'air_date', 'rating', 'is_featured')
    list_filter = ('season', 'is_featured', 'air_date')
    search_fields = ('title', 'original_title', 'director', 'writer')
    list_editable = ('is_featured',)
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'original_title', 'season', 'episode_number')
        }),
        ('Даты и рейтинги', {
            'fields': ('air_date', 'rating')
        }),
        ('Описание', {
            'fields': ('short_description', 'description')
        }),
        ('Съёмочная группа', {
            'fields': ('director', 'writer')
        }),
        ('Дополнительно', {
            'fields': ('is_featured',),
            'classes': ('collapse',)
        })
    )
    actions = ['mark_as_featured', 'unmark_featured']

    def mark_as_featured(self, request, queryset):
        queryset.update(is_featured=True)
    mark_as_featured.short_description = 'Отметить выбранные эпизоды как избранные'

    def unmark_featured(self, request, queryset):
        queryset.update(is_featured=False)
    unmark_featured.short_description = 'Снять отметку "избранное"'
