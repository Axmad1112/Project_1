# Generated by Django 3.1.5 on 2021-03-27 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecover', '0018_auto_20210317_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseFooter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter_link', models.CharField(max_length=50)),
                ('facebook_link', models.CharField(max_length=50)),
                ('instagram_link', models.CharField(max_length=50)),
                ('telegram_link', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='address',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='announcement',
            name='price',
            field=models.CharField(choices=[('5000', '5000'), ('10000', '10000'), ('50000', '50000'), ('100000', '100000'), ('200000', '200000'), ('300000', '300000'), ('400000', '400000'), ('500000', '500000'), ('600000', '600000'), ('700000', '700000'), ('800000', '800000'), ('900000', '900000'), ('1000000', '1000000'), ('2000000', '2000000')], max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]