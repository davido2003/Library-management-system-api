# Generated by Django 3.2.10 on 2022-09-13 17:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0005_bookorder'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookOrder',
            new_name='BookReturn',
        ),
    ]
