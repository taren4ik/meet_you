from datetime import date

from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()


class Category(models.Model):
    """Модель для определения категории."""

    name = models.CharField(
        max_length=256, unique=True, verbose_name='Название '
                                                             'категории'
    )
    slug = models.SlugField(
        max_length=50, unique=True, verbose_name='slug категории'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'Category {self.name}, slug {self.slug}'


class Profile(models.Model):
    """Модель для определения профайла."""

    name = models.CharField(max_length=100, verbose_name='Имя пользователя')

    phone = PhoneNumberField(null=False, unique=True)
    image = models.ImageField(verbose_name='Изображение')

    description = models.TextField(
        blank=True, verbose_name='Описание анкеты'
    )

    year = models.PositiveSmallIntegerField(
        db_index=True, validators=[MaxValueValidator(date.today().year)],
        verbose_name='Год рождения'
    )
    description = models.TextField(
        blank=True, verbose_name='описание произведения'
    )
    category = models.ForeignKey(
        Category, blank=True, null=True,
        on_delete=models.SET_NULL,
        verbose_name='Категория',
        related_name='titles'
    )

    class Meta:
        ordering = ('category', 'name')
        verbose_name = 'Профайл'
        verbose_name_plural = 'Профайлы'

    def __str__(self):
        return f'Name {self.name}, phone: {self.phone}, born: {self.year}'


class Follow(models.Model):
    """Модель для определения профайла."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="follower",
        verbose_name="Подписчик",
        help_text="Пользователь, который подписывается",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following",
        verbose_name="Автор",
        help_text="Автор, на которого подписываются",

    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'author'],
                                    name='unique_following')
        ]
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f'Follow(pk={self.pk}, author={self.user},{self.author})'


class Comment(models.Model):
    """Модель для определения профайла."""

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='comments'
    )
    text = models.TextField(max_length=2000)
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
    )

    class Meta:
        ordering = ('author',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'Comment(pk={self.pk}, text={self.text}, group={self.author})'
