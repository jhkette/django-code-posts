# Generated by Django 2.2.4 on 2019-08-12 13:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190812_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 12, 13, 19, 8, 705645), verbose_name='date published'),
        ),
    ]
