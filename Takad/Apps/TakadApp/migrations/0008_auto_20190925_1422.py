# Generated by Django 2.2.5 on 2019-09-25 11:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TakadApp', '0007_auto_20190925_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reports_result',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 25, 14, 22, 52, 525722)),
        ),
    ]
