# Generated by Django 3.1.1 on 2020-10-04 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201004_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tags',
            name='slug',
            field=models.SlugField(),
        ),
    ]
