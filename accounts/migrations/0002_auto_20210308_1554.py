# Generated by Django 3.1.5 on 2021-03-08 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='author_image',
            field=models.ImageField(default='<user.first_name[0]>', upload_to='author_image'),
        ),
    ]
