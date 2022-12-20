from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя', blank=False)
    surname = models.CharField(max_length=120, verbose_name='Фамилия', blank=False)
    patronymic = models.CharField(max_length=120, verbose_name='Отчество', blank=False)


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название', blank=False)
    author = models.ForeignKey(Author, max_length=100, verbose_name='Автор', blank=False, on_delete=models.CASCADE)
    publishing_office = models.CharField(max_length=100, verbose_name='Издательство')
    year_of_rel = models.IntegerField(verbose_name='Год выпуска', blank=False,
                                    validators=[MinValueValidator(1000), MaxValueValidator(2022)])
    genre = models.CharField(max_length=200, verbose_name='Жанр', blank=True)
    category = models.CharField(max_length=200, verbose_name='Категория', blank=True)

    class Meta:
        unique_together = ('title', 'author', 'year_of_rel', 'publishing_office')
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'