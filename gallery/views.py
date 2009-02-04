from django.shortcuts import render_to_response
from nevermatter.gallery.models import Exhibit
import random

def overview(request):
    watcha = "hiya!"
    images = []
    image_objects = Exhibit.objects.all()
    for index in range(4):
        images.append(random.choice(image_objects).square_image_url())
    return render_to_response('gallery/index.html', locals())
    
def exhibit(request, exhibit_index):
    main_image_url = Exhibit.objects.all()[exhibit_index].image_file.url
    number_of_images = Exhibit.objects.count()
    
    navigation_image_urls = []
    navigation_image_indices = []
    for i in range(7):
        current_index = image_index - 3
        if current_index < 0 or current_index >= number_of_images:
            navigation_image_urls.append(None)
            navigation_image_urls.append(None)
        else:
            navigation_image_urls.append(Exhibit.objects.all()[current_index].image_file.url)
            navigation_image_indices.append(current_index)
    
    return render_to_response('gallery/image.html', locals())