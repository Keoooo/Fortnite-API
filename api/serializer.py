from rest_framework import serializers 
from .models import fortniteskins

class SkinSerializer(serializers.ModelSerializer):
	outfit_img = serializers.ImageField(max_length=None, allow_empty_file=True, allow_null=True, required=False)

	class Meta:
		model = fortniteskins
		fields = ('id', 'name', 'season', 'rarity', 'price', 'outfit_img')