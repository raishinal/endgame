# Generated by Django 2.2.2 on 2019-06-23 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20190623_0906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='genre',
        ),
    ]
