from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
	title = models.CharField('Movie\'s title', max_length=255)
	year = models.PositiveIntegerField(default=2019)
	rated = models.CharField(max_length=64)
	released_on = models.DateField('Release Date')
	genre = models.CharField(max_length=255)
	director = models.CharField(max_length=255)
	plot = models.TextField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)

	def __str__(self):
		return self.title

RATING_CHOICES = ((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'))

class Review(models.Model):
	movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
	rating = models.IntegerField(choices=RATING_CHOICES)
	text = models.TextField()
	user = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.movie.title