# Generated by Django 3.1.5 on 2021-02-22 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecover', '0002_auto_20210222_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='text',
            field=models.TextField(max_length=100),
        ),
    ]