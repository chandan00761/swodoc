# Generated by Django 3.2.9 on 2021-12-14 17:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20211213_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 12, 14, 23, 15, 1, 795323)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 12, 14, 23, 15, 7, 635449)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='project',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 12, 14, 23, 15, 14, 3384)),
            preserve_default=False,
        ),
    ]
