# Generated by Django 4.0.1 on 2022-01-08 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0013_alter_song_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='description',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
