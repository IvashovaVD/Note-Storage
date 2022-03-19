from typing import Final, final

from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class Folder(models.Model):
    num_user = models.ForeignKey(User, related_name='folders', verbose_name='nick', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="доска",
                            verbose_name='название доски для заметок')
    release_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]
        unique_together = ('name', 'num_user')

    def __str__(self):
        return self.name


class Note(models.Model):
    num_folder = models.ForeignKey(Folder, related_name='notes', verbose_name='Название папки',
                                   on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="Заметка", verbose_name='Название заметки')
    textn = models.TextField(blank=True, verbose_name='Текст заметки')
    urln = models.URLField(blank=True, verbose_name='Вставить ссылку на объект')
    available = models.BooleanField(verbose_name='Скрыть объект для других пользователей')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["updated_at", "created_at"]
        unique_together=('name', 'num_folder')

    def __str__(self):
        return self.name
