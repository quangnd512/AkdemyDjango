from django.db import models
from datetime import datetime

from ckeditor.fields import RichTextField

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.title
    
