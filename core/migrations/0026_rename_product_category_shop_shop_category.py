# Generated by Django 4.1.7 on 2023-05-08 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_shopcategory_shop'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='product_category',
            new_name='shop_category',
        ),
    ]
