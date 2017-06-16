from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blogger(models.Model):
	"""
	Model representing a blogger
	"""
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=200)
	bio = models.CharField(max_length=500)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		pass


class Blogpost(models.Model):
	"""
	Model representing a blog post
	"""
	post_date = models.DateField()
	author = models.ForeignKey('Blogger', on_delete=models.CASCADE, null=True)
	description = models.CharField(max_length=5000)
	title = models.CharField(max_length=100)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		pass

class Comment(models.Model):
	"""
	Model representing a comment on a blog
	"""
	commenter = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	description = models.CharField(max_length=500)
	blogpost = models.ForeignKey('Blogpost', on_delete=models.CASCADE, null=True)

	def get_absolute_url(self):
		pass

	def __str__(self):
		if(len(self.description)>75):
			return self.description[:75]
		return self.description