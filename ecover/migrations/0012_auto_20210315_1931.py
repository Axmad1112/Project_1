# Generated by Django 3.1.5 on 2021-03-15 14:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecover', '0011_auto_20210314_1112'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.AlterField(
            model_name='announcement',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 3, 15, 19, 31, 5, 448982)),
        ),
    ]