# Generated by Django 4.2.5 on 2023-11-13 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='author',
            name='no_of_articles',
        ),
    ]
