# Generated by Django 2.1.7 on 2019-07-22 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New_Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='media/image')),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
