from django.db import models

# Create your models here.


class season(models.Model):
	season = models.IntegerField()
	date = models.DateField()
	season_theme = models.CharField(max_length=200)

	def __str__(self):
		return self.season_theme


class fortniteskins(models.Model):
	name = models.CharField(max_length=200)
	season = models.ForeignKey(season, on_delete=models.CASCADE)
	rarity = models.CharField(max_length=20)
	price = models.IntegerField()
	first_seen = models.DateField()
	outfit_img = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.name

		