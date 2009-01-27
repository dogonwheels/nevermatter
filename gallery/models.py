from django.db import models

# Create your models here.
class Image(models.Model):
    image_file = models.ImageField(upload_to='media')
    title = models.CharField(max_length=200)
    description = models.TextField()
