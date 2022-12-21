# Generated by Django 4.1.2 on 2022-12-20 11:37

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.CharField(blank=True, max_length=200, verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(blank=True, max_length=200, verbose_name='Жанр'),
        ),
        migrations.AddField(
            model_name='book',
            name='publishing_office',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, verbose_name='Издательство'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='year_of_rel',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(2022)], verbose_name='Год выпуска'),
        ),
        migrations.AlterUniqueTogether(
            name='book',
            unique_together={('title', 'author', 'year_of_rel', 'publishing_office')},
        ),
    ]