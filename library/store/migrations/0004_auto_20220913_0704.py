# Generated by Django 3.2.10 on 2022-09-13 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20190812_1748'),
    ]

    operations = [
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User', models.CharField(max_length=100)),
                ('Library', models.CharField(max_length=100)),
                ('Book', models.CharField(max_length=100)),
                ('Librarian', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='BookOrder',
        ),
    ]
