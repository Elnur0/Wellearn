# Generated by Django 4.1.7 on 2023-04-25 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Subscribers',
            },
        ),
    ]
