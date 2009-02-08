from django.db import models
from django.conf import settings
import os
import Image

class Exhibit(models.Model):
    image_file = models.ImageField(upload_to='uploads')
    title = models.CharField(max_length=200)
    description = models.TextField()

    def _prefix_path(self, prefix, full_filename):
        (path, filename) = os.path.split(full_filename)
        return os.path.join(path, prefix + filename)
    
    @property
    def _small_image_filename(self):
        return self._prefix_path('small_', self.image_file.file.name)

    @property
    def _medium_image_filename(self):
        return self._prefix_path('medium_', self.image_file.file.name)

    @property
    def _large_image_filename(self):
        return self._prefix_path('large_', self.image_file.file.name)

    @property
    def small_image_url(self):
        return self._prefix_path('small_', self.image_file.url)

    @property
    def medium_image_url(self):
        return self._prefix_path('medium_', self.image_file.url)

    @property
    def large_image_url(self):
        return self._prefix_path('large_', self.image_file.url)

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
            
            large_image = square_image.resize((500, 500), Image.ANTIALIAS)
            large_image.save(self._large_image_filename, quality=90)
            
            medium_image = square_image.resize((300, 300), Image.ANTIALIAS)
            medium_image.save(self._medium_image_filename, quality=90)
            
            small_image = square_image.resize((100, 100), Image.ANTIALIAS)
            small_image.save(self._small_image_filename, quality=90)
            
    def delete(self):
        image_files = [self._small_image_filename, self._medium_image_filename, self._large_image_filename]
        for filename in image_files:
            if not filename == '':
                os.remove(filename)
        
        super(Exhibit, self).delete()
    
    def __unicode__(self):
        return self.title
