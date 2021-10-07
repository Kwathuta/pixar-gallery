from django.db import models

# Create your models here.


class Image(models.Model):
    image = models.ImageField(upload_to='gallery/', default=None)
    name = models.CharField(max_length=30)
    description = models.TextField()


class Location(models.Model):
    name = models.CharField(max_length=30)


class Category(models.Model):
    name = models.CharField(max_length=30)
