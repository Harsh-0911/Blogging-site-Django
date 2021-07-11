from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Article(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
	title = models.CharField(max_length = 220, unique = True)
	slug = models.SlugField(max_length = 220, unique = True, blank=True)
	content = models.TextField()
	created_on = models.DateField(auto_now_add=True)

	def save(self, *args, **kwargs):
		value = self.title
		self.slug = slugify(value, allow_unicode=True)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.title
