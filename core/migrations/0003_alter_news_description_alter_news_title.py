# Generated by Django 4.1.7 on 2023-03-08 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_category_options_alter_news_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(blank=True, help_text='for the data', null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]