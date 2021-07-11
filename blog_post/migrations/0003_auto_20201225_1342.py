# Generated by Django 3.1.4 on 2020-12-25 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_post', '0002_auto_20201225_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, max_length=220, unique=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=220, unique=True),
        ),
    ]
