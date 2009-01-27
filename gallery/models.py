from django.db import models

# Create your models here.
class Image(models.Model):
    image_file = models.ImageField(upload_to='uploads/%Y/%m/%d')
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    def __unicode__(self):
        return self.title
