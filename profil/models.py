from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.template.defaultfilters import slugify

# Create your models here.


class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=50)
	content= models.TextField()
	def __str__(self):
		return self.title

class Person(models.Model):
        # users_photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
        name = models.CharField(max_length=50, default='')
        # gender = models.CharField(max_length=30)
        # date_of_birth = models.DateField(max_length=30)
        # telegram = models.CharField(max_length=30)
        # nom_tel = models.IntegerField()
        # osebe = models.CharField(max_length=30)
        # student = models.CharField(max_length=30)
        # curs = models.CharField(max_length=30)
        # stupen_obrazov = models.CharField(max_length=30)
        # facultet = models.CharField(max_length=30)
        # obrazov_pr = models.CharField(max_length=30)
        # rabota = models.CharField(max_length=30)




