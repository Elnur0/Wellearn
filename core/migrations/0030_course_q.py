# Generated by Django 4.1.7 on 2023-05-26 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_faq'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='Q',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
