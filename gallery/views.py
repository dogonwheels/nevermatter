from django.shortcuts import render_to_response
from nevermatter.gallery.models import Exhibit
import random

def overview(request):
    image_objects = Exhibit.objects.all()
    images = random.sample(image_objects, min(len(image_objects), 4))
    
    return render_to_response('gallery/index.html', locals())
    
def exhibit(request, exhibit_id):
    main_image = Exhibit.objects.get(id=exhibit_id)
    images = Exhibit.objects.all()
    
    return render_to_response('gallery/image.html', locals())
    
def contact(request):
    return render_to_response('gallery/contact.html', locals())