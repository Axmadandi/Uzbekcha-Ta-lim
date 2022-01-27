from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blogs(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField('Name',max_length=200)
	body = models.TextField('Body')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Blogs"
		verbose_name_plural = 'Blogslar'
	
