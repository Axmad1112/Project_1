# Generated by Django 3.1.5 on 2021-02-05 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecover', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='image_person',
        ),
    ]
