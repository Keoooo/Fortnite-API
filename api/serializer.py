from rest_framework import serializers 
from .models import fortniteskins, season

"""Converts models to JSON """

class SkinSerializer(serializers.HyperlinkedModelSerializer):
	outfit_img = serializers.ImageField(max_length=None, allow_empty_file=True, allow_null=True, required=False)
	class Meta:
		model = fortniteskins
		fields = ('id', 'name', 'season', 'rarity', 'price', 'outfit_img', 'first_seen')

class SeasonSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = season
		fields = ('id', 'date', 'season_theme')


