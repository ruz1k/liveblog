# Generated by Django 3.0 on 2020-04-16 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exampleproject', '0006_auto_20200219_0120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
    ]
