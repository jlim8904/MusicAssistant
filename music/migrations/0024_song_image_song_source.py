# Generated by Django 4.0.1 on 2022-01-09 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0023_alter_song_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='image',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='song',
            name='source',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
