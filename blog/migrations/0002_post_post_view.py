# Generated by Django 3.1.5 on 2021-03-22 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_view',
            field=models.IntegerField(default=0),
        ),
    ]
