# Generated by Django 3.0 on 2020-04-16 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exampleproject', '0008_auto_20200416_1922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_date',
        ),
    ]