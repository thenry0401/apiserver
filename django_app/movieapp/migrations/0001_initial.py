# Generated by Django 2.1.1 on 2018-09-04 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieInfo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('imdb_code', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('title_english', models.CharField(max_length=30)),
                ('title_long', models.CharField(max_length=30)),
                ('slug', models.CharField(max_length=30)),
                ('year', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('runtime', models.IntegerField()),
                ('genres', models.CharField(max_length=30)),
                ('summary', models.TextField()),
                ('decription_full', models.TextField()),
                ('synopsis', models.TextField()),
                ('yt_trailer_code', models.CharField(max_length=30)),
                ('language', models.CharField(max_length=30)),
                ('mpa_rating', models.CharField(max_length=30)),
                ('background_image', models.ImageField(upload_to='')),
                ('background_image_original', models.ImageField(upload_to='')),
                ('small_cover_image', models.ImageField(upload_to='')),
                ('medium_cover_image', models.ImageField(upload_to='')),
                ('large_cover_image', models.ImageField(upload_to='')),
                ('state', models.CharField(max_length=30)),
                ('date_uploaded', models.DateTimeField()),
                ('date_uploaded_unix', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Torrent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('hash', models.CharField(max_length=200)),
                ('quality', models.CharField(max_length=10)),
                ('seeds', models.IntegerField()),
                ('peers', models.IntegerField()),
                ('size', models.CharField(max_length=10)),
                ('size_bytes', models.IntegerField()),
                ('date_uploaded_unix', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='movieinfo',
            name='torrents',
            field=models.ManyToManyField(to='movieapp.Torrent'),
        ),
    ]
