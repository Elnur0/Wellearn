# Generated by Django 4.1.7 on 2023-05-04 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_product_is_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name': 'Shop Category',
                'verbose_name_plural': 'Shop Category',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
                ('descriptions', models.TextField()),
                ('image', models.ImageField(upload_to='products')),
                ('price', models.IntegerField()),
                ('is_published', models.BooleanField(default=True)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.shopcategory')),
            ],
            options={
                'verbose_name': 'Shops',
                'verbose_name_plural': 'Shops',
            },
        ),
    ]