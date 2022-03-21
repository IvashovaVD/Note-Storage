from typing import Final, final

from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.db.models.signals import post_delete, pre_delete
from django.dispatch import receiver


def user_directory_path(instance, filename):
    return instance.tagging + '/' + filename


class Folder(models.Model):
    num_user = models.ForeignKey(User, related_name='folders', verbose_name='nick', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="доска",
                            verbose_name='название доски для заметок')
    release_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]
        constraints = [models.UniqueConstraint(fields=['name', 'num_user'], name="user_namef")]

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
        constraints = [models.UniqueConstraint(fields=['name', 'num_folder'], name="user_namen")]

    def __str__(self):
        return self.name


class FileNote(models.Model):
    num_folder = models.ForeignKey(Folder, related_name='files', verbose_name='Название папки',
                                   on_delete=models.CASCADE)
    NOTE_CHOICES = [
        ('h', 'home'),
        ('w', 'work'),
        ('t', 'travel'),
        ('s', 'study'),
        ('p', 'project'),
        ('o', 'other'),
    ]
    tagging = models.CharField(max_length=1,
                               choices=NOTE_CHOICES,
                               verbose_name='Примечание')
    created_at = models.DateTimeField(auto_now_add=True)
    filen = models.FileField(upload_to=user_directory_path, verbose_name='Загрузить файл')

    def __str__(self):
        return self.tagging


@receiver(pre_delete, sender=FileNote)
def FileNote_delete(sender, instance, **kwargs):
    instance.filen.delete(False)
