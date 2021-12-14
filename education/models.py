from random import randint

import lorem
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100, blank=True, verbose_name='Назва')
    image = models.ImageField(upload_to='images', blank=True, verbose_name='Зображення')
    annotation = models.TextField(blank=True, verbose_name='Аннотація')
    text = models.TextField(blank=True, verbose_name='Текст')
    lectures_number = models.IntegerField(default=1, verbose_name='Кількість лекцій')
    start = models.DateTimeField(verbose_name='Початок')
    end = models.DateTimeField(verbose_name='Завершення')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'курси'
        ordering = ('start', 'name')

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = lorem.sentence()[:-1]
        if not self.annotation:
            self.annotation = lorem.sentence() * randint(1, 3)
        if not self.text:
            self.text = lorem.text() * randint(2, 5)
        if not self.image:
            self.image = '../media/images/you_course.png'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
