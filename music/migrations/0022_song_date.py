# Generated by Django 4.0.1 on 2022-01-09 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0021_rename_url_song_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
