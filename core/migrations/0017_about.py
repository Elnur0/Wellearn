# Generated by Django 4.1.7 on 2023-04-22 08:41

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_remove_test_title_az_remove_test_title_en_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('description', ckeditor.fields.RichTextField(blank=True, help_text='for the data', null=True)),
                ('image', models.ImageField(upload_to='media/about')),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'About',
            },
        ),
    ]
