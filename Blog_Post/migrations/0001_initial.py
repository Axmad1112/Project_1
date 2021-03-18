# Generated by Django 3.1.5 on 2021-03-17 08:49

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ecover', '0017_auto_20210316_1123'),
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post_categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('post_image', models.ImageField(upload_to='blog_rasm')),
                ('post_single_image1', models.ImageField(upload_to='blog_rasm')),
                ('content_header', models.TextField(max_length=1000)),
                ('post_single_image2', models.ImageField(upload_to='blog_rasm')),
                ('content_body', models.TextField(max_length=1000)),
                ('paragraph', models.TextField(max_length=500)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('time', models.TimeField(auto_now_add=True, null=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecover.agent')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog_Post.post_categories')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
