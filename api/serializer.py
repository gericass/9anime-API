from rest_framework import serializers
from .models import animedb

class animedbSerializer(serializers.ModelSerializer):
    class Meta:
        model = animedb
        fields = ('title','title_jp','year','season','weekday','url')
