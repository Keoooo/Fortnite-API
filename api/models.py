from django.db import models

# Create your models here.

class fortniteskins(models.Model):
	name = models.CharField(max_length=200)
	season = models.IntegerField()
	rarity = models.CharField(max_length=20)
	price = models.IntegerField()
	outfit_img = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.name