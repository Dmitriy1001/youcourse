# Generated by Django 2.1 on 2021-04-26 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_course_lectures_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='annotation',
            field=models.TextField(blank=True, verbose_name='Аннотація'),
        ),
        migrations.AlterField(
            model_name='course',
            name='end',
            field=models.DateTimeField(verbose_name='Завершення'),
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, upload_to='images', verbose_name='Зображення'),
        ),
        migrations.AlterField(
            model_name='course',
            name='lectures_number',
            field=models.IntegerField(default=1, verbose_name='Кількість лекцій'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Назва'),
        ),
        migrations.AlterField(
            model_name='course',
            name='start',
            field=models.DateTimeField(verbose_name='Початок'),
        ),
        migrations.AlterField(
            model_name='course',
            name='text',
            field=models.TextField(blank=True, verbose_name='Текст'),
        ),
    ]
