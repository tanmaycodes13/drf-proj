from rest_framework import serializers
from .models import tv_series, netflix_seires


class TvSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source="creator.username")

    class Meta:
        model = tv_series
        fields = ("id", "title", "genre", "year", "rating", "creator")


class NetflixSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source="creator.username")

    class Meta:
        model = netflix_seires
        fields = ("id", "title", "genre", "year", "rating", "creator")
