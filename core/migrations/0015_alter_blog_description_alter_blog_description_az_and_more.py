# Generated by Django 4.1.7 on 2023-04-09 06:49

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_test_title_az_test_title_en'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, help_text='for the data', null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description_az',
            field=ckeditor.fields.RichTextField(blank=True, help_text='for the data', null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description_en',
            field=ckeditor.fields.RichTextField(blank=True, help_text='for the data', null=True),
        ),
    ]
