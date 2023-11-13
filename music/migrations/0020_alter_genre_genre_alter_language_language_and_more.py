# Generated by Django 4.0.1 on 2022-01-08 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0019_remove_singer_area_delete_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='genre',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='language',
            name='language',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='singer',
            name='singer',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='singer_type',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]