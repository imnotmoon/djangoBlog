# Generated by Django 3.0.8 on 2020-07-18 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_articles_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='author',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='password',
        ),
    ]
