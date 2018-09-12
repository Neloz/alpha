from django.db import models

# Create your models here.
class Users(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField()
	staff = models.BooleanField(default=False)
	def __str__(self):
		return self.title


class Trans(models.Model):
	tipo = models.CharField(max_length=20)
	date = models.DateTimeField()
	lugar = models.CharField(max_length=30)
	username = models.CharField(max_length=30)
	n_cuenta = models.IntegerField()
	status = models.CharField(max_length=20)

	def __str__(self):
		return self.username + ' ___Tipo de transaccion: ' + self.tipo
