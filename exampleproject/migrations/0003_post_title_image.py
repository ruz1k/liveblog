# Generated by Django 3.0 on 2020-01-02 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exampleproject', '0002_auto_20190722_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_image',
            field=models.ImageField(null=True, upload_to='media/title_image'),
        ),
    ]
