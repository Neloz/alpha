from django.db import models

# Create your models here.
class Users(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField()
	staff = models.BooleanField(default=False)
	def __str__(self):
		return self.title