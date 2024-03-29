# Generated by Django 3.1.5 on 2021-03-27 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecover', '0019_auto_20210327_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basefooter',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='basefooter',
            name='facebook_link',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='basefooter',
            name='instagram_link',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='basefooter',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='basefooter',
            name='telegram_link',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='basefooter',
            name='twitter_link',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
