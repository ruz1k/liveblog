from django.db import models
from django.conf import settings

class HomePage(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()