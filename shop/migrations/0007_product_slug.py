# Generated by Django 3.2.4 on 2021-06-22 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20210622_0604'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=155)),
        ),
    ]