# Generated by Django 2.2.10 on 2021-05-14 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yt_search', '0004_auto_20210514_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='description',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]
