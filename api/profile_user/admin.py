from django.contrib import admin

from .models import (Follow, Category, Comment, Profile)


class ProfileAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('author', 'phone', 'category')
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('phone',)
    # Добавляем возможность фильтрации по дате
    list_filter = ('phone', 'author',)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Follow)
admin.site.register(Category)
admin.site.register(Comment)
