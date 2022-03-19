# Generated by Django 3.2.12 on 2022-03-19 07:59

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='folder',
            unique_together={('name', 'num_user')},
        ),
        migrations.AlterUniqueTogether(
            name='note',
            unique_together={('name', 'num_folder')},
        ),
    ]
