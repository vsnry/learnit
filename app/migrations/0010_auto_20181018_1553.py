# Generated by Django 2.1.1 on 2018-10-18 20:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20181018_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 18, 20, 53, 26, 661977, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='list',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 18, 20, 53, 26, 660977, tzinfo=utc)),
        ),
    ]
