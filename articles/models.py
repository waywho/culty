from django.db import models

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField()
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default='defaul.png', blank=True)
	# add author

	def __str__(self):
		return self.title

	def snippet(self):
		return self.body[:50] + "..."