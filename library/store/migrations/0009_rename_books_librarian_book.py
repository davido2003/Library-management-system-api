# Generated by Django 3.2.10 on 2022-09-13 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20220913_1047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='librarian',
            old_name='books',
            new_name='Book',
        ),
    ]
