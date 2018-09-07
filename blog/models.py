from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
	writer =  models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title  =  models.CharField(max_length=100, unique=True)
	text   =  models.TextField()
	posted_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title


