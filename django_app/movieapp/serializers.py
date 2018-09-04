from rest_framework import serializers

from movieapp.models import MovieInfo, Torrent


class MovieSerializer(serializers.ModelSerializer):
    torrents = serializers.SerializerMethodField

    class Meta:
        model = MovieInfo
        fields = (
            'id',
            'url',
            'imdb_code',
            'title',
            'title_english',
            'slug',
            'year',
            'rating',
            'runtime',
            'genres',
            'summary',
            'description_full',
            'synopsis',
            'yt_trailer_code',
            'language',
            'mpa_rating',
            'background_image',
            'background_image_original',
            'small_cover_image',
            'medium_cover_image',
            'large_cover_image',
            'state',
            'torrents',
            'date_uploaded',
            'date_uploaded_unix',
        )

    def get_torrents(self, obj):
        return TorrentSerializer(many=True).data


class TorrentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Torrent
        fields = (
            'url',
            'hash',
            'quality',
            'seeds',
            'peers',
            'size',
            'size_bytes',
            'date_uploaded',
            'date_uploaded_unix',
        )