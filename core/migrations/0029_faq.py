# Generated by Django 4.1.7 on 2023-05-26 15:57

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_course_title_two'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('question', ckeditor.fields.RichTextField(max_length=300, verbose_name='Sual')),
                ('answer', ckeditor.fields.RichTextField(max_length=10000, verbose_name='Cavab')),
                ('order', models.IntegerField(default=0, verbose_name='Sıra')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
    ]
