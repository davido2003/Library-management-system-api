# Generated by Django 3.2.10 on 2022-09-13 17:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_rename_bookorder_bookreturn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookreturn',
            name='books',
        ),
        migrations.AddField(
            model_name='bookreturn',
            name='Book',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
