# Generated by Django 2.1.1 on 2018-10-18 20:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20181018_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 18, 20, 59, 9, 990614, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='list',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 18, 20, 59, 9, 990614, tzinfo=utc)),
        ),
    ]
