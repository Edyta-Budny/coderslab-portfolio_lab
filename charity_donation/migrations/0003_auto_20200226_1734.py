# Generated by Django 2.2.4 on 2020-02-26 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity_donation', '0002_auto_20200226_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='pick_up_time',
            field=models.TimeField(),
        ),
    ]
