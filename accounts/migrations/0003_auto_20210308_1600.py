# Generated by Django 3.1.5 on 2021-03-08 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210308_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='author_image',
            field=models.ImageField(default='author.jpg', upload_to='author_image'),
        ),
    ]
