from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    