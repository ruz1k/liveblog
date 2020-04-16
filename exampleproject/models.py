from django.conf import settings
from django.db import models
from django.utils import timezone
from django.db.models import ImageField

class Post(models.Model):
	title = models.CharField(max_length=200)
	title_image = models.ImageField(upload_to='media/title_image', null=True)
	text = models.TextField()
	image = models.ImageField(upload_to='media/image',blank=True)
	image1 = models.ImageField(upload_to='media/image', blank=True)
	image2 = models.ImageField(upload_to='media/image', blank=True)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
