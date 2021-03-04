# Generated by Django 3.1.5 on 2021-03-03 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecover', '0005_cityproperties'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='image',
            field=models.ImageField(default='', upload_to='region-image'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='CityProperties',
        ),
    ]