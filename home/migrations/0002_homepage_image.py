# Generated by Django 2.2.3 on 2019-07-28 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='image',
            field=models.ImageField(null=True, upload_to='media/image'),
        ),
    ]
