# Generated by Django 4.0.1 on 2022-01-08 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0011_alter_song_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='url',
            field=models.URLField(default='DEFAULT VALUE', max_length=1000),
        ),
    ]