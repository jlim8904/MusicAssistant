# Generated by Django 4.0.1 on 2022-01-09 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0028_alter_song_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.CharField(default='aimer.jpg', max_length=100),
        ),
    ]