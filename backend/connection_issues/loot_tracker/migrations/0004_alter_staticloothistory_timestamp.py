# Generated by Django 3.2.5 on 2021-08-09 20:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loot_tracker', '0003_auto_20210810_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticloothistory',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 10, 3, 51, 38, 742490)),
        ),
    ]
