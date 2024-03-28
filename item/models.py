from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=255)
	
	class Meta:
		verbose_name_plural ='Categories'

	def __str__(self):
		return self.name
	
class Item(models.Model):
	category = models.ForeignKey(Category, related_name='items',on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	description = models.TextField(blank=True, null=True)
	price = models.FloatField()
	image = models.ImageField(upload_to='items_images', blank=True, null=True)
	is_sold = models.BooleanField(default=False)
	created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
	created_at =models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.name
	

# class Review(models.Model):
# 	product = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='reviews')
# 	text = models.TextField(blank=True, null=True)	
# 	created_user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
# 	created_time = models.DateTimeField(auto_now_add=True)
