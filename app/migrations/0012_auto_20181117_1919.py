# Generated by Django 2.1.1 on 2018-11-18 00:19

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0011_auto_20181018_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='user',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 18, 0, 17, 23, 909230, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='list',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 18, 0, 17, 23, 909230, tzinfo=utc)),
        ),
    ]
