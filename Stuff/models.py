from django.db import models

# Create your models here.

class TargetObject(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    models.ImageField(blank=True, upload_to='images/target_object/')
    def __str__(self):
        return self.content
    

class ReasonToChooseUs(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    models.ImageField(blank=True, upload_to='images/reason_to_choose_us/')
    def __str__(self):
        return self.content