# Generated by Django 3.2.3 on 2021-05-16 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yt_search', '0009_videos_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videos',
            name='created',
        ),
    ]
