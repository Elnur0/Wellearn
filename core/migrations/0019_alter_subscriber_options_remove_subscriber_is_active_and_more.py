# Generated by Django 4.1.7 on 2023-04-25 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_subscriber'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscriber',
            options={'verbose_name': 'Subscribers', 'verbose_name_plural': 'Subscribers'},
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='message',
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='name',
        ),
    ]
