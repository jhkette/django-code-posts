# Generated by Django 2.2.4 on 2019-08-12 13:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190812_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 12, 13, 37, 1, 7209), verbose_name='date published'),
        ),
    ]
