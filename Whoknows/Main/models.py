from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Topic(models.Model):
	title = models.CharField(max_length=255)
	author = models.ForeignKey(User,on_delete=models.CASCADE)
	content = models.TextField()
	created_at = models.DateTimeField(default=timezone.now)
	updated_at = models.DateTimeField(auto_now=True)


	def __str__(self):
		return f'{self.title} by {self.author}'