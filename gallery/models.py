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
        # This is duplicated, and subject to borkage if the filename contains '.'s!
        return self.image_file.file.name.replace('.', '_square.')
    
    def square_image_url(self):
        return self.image_file.url.replace('.', '_square.')
    
    def save(self, force_insert=False, force_update=False):
        super(Exhibit, self).save(force_insert, force_update)
        filename = self.image_file.file.name
        if not filename == '':
            original_image = Image.open(filename)
            smallest_dimension = min(original_image.size)
            offset = ((smallest_dimension - original_image.size[0]) / 2, 
                      (smallest_dimension - original_image.size[1]) / 2)

            square_image = Image.new(original_image.mode, (smallest_dimension, smallest_dimension))
            square_image.paste(original_image, offset)
            
            square_300_image = square_image.resize((300, 300), Image.ANTIALIAS)
            square_image_filename = self.square_image_filename()
            square_300_image.save(square_image_filename)
        
    def delete(self):
        filename = self.square_image_filename()
        if not filename == '':
            os.remove(filename)
        
        super(Exhibit, self).delete()
    
    def __unicode__(self):
        return self.title
