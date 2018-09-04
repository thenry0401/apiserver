from django.db import models


class MovieInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    url = models.URLField()
    imdb_code = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    title_english = models.CharField(max_length=30)
    title_long = models.CharField(max_length=30)
    slug = models.CharField(max_length=30)
    year = models.IntegerField()
    rating = models.IntegerField()
    runtime = models.IntegerField()
    genres = models.CharField(max_length=30)
    summary = models.TextField()
    decription_full = models.TextField()
    synopsis = models.TextField()
    yt_trailer_code = models.CharField(max_length=30)
    language = models.CharField(max_length=30)
    mpa_rating = models.CharField(max_length=30)
    background_image = models.ImageField()
    background_image_original = models.ImageField()
    small_cover_image = models.ImageField()
    medium_cover_image = models.ImageField()
    large_cover_image = models.ImageField()
    state = models.CharField(max_length=30)
    torrents = models.ManyToManyField('Torrent')
    date_uploaded = models.DateTimeField()
    date_uploaded_unix = models.IntegerField()


class Torrent(models.Model):
    url = models.URLField()
    hash = models.CharField(max_length=200)
    quality = models.CharField(max_length=10)
    seeds = models.IntegerField()
    peers = models.IntegerField()
    size = models.CharField(max_length=10)
    size_bytes = models.IntegerField()
    date_uploaded = models.DateTimeField
    date_uploaded_unix = models.IntegerField()
