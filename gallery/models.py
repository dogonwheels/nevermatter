from django.db import models
from django.conf import settings
import os
import Image

# Create your models here.
class Exhibit(models.Model):
    image_file = models.ImageField(upload_to='uploads')
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    def square_image_filename(self):
        return self.image_file.file.name.replace('.', '_square.jpg')
    
    def save(self, force_insert=False, force_update=False):
        super(Exhibit, self).save(force_insert, force_update)
        filename = self.image_file.file.name
        if not filename == '':
            square_image = Image.open(filename)
            
            square_image.thumbnail((300, 300), Image.ANTIALIAS)
            square_image_filename = self.square_image_filename()
            square_image.save(square_image_filename)
        
    def delete(self):
        filename = self.square_image_filename()
        if not filename == '':
            os.remove(filename)
        
        super(Exhibit, self).delete()
    
    def __unicode__(self):
        return self.title
