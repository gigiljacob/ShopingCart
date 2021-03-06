# Generated by Django 3.2.4 on 2021-06-20 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='show',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=155)),
                ('descritpion', models.TextField(max_length=255)),
                ('mrp', models.PositiveIntegerField()),
                ('discount', models.FloatField()),
                ('price', models.PositiveIntegerField()),
                ('in_stock', models.BooleanField(default=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.productcategory')),
            ],
        ),
    ]
