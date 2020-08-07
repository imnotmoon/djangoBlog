# Generated by Django 2.1.1 on 2020-08-07 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title', max_length=200)),
                ('name', models.CharField(default='bigmac', max_length=200)),
                ('mood', models.IntegerField(default=1)),
                ('image', models.CharField(max_length=400, null=True)),
            ],
        ),
    ]
