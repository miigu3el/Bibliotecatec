# Generated by Django 4.2.5 on 2023-09-15 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='site_autor',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='editora',
            name='site_editora',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]