# Generated by Django 2.2.5 on 2019-09-25 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TakadApp', '0021_auto_20190925_1947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scan',
            name='report',
        ),
        migrations.RemoveField(
            model_name='reports_result',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='reports_result',
            name='hash_scan',
        ),
        migrations.DeleteModel(
            name='Reports',
        ),
        migrations.DeleteModel(
            name='Scan',
        ),
    ]
