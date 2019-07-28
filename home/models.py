from django.db import models
from django.conf import settings

class HomePage(models.Model):
	title = models.CharField(max_length=200)
	image = models.ImageField(upload_to='media/image',null=True)
	text = models.TextField()