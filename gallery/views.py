from django.core.files.images import get_image_dimensions
from django.shortcuts import render

from helpers.navbar.context import navigation_sections
from picture.models import Picture
from gallery.models import Gallery


def gallery(request, gallery_name):
    pictures_for_gallery = Picture.objects.filter(gallery__name=gallery_name)
    for picture in pictures_for_gallery:
        width, height = get_image_dimensions(picture.picture.file)
        picture.width = width
        picture.height = height
        # print('picture:', picture)
        # print('picture.width:', picture.width)
        # print('picture.height:', picture.height)

    if gallery_name == 'Me':
        context = {
            'sections': navigation_sections(),
            'picture': pictures_for_gallery[0]
        }
        return render(request, 'pages/about.html', context)
    else:
        gallery = Gallery.objects.filter(name=gallery_name).order_by('date')
        context = {
            'sections': navigation_sections(),
            'gallery': gallery[0],
            'pictures': pictures_for_gallery
        }
        return render(request, 'pages/gallery.html', context)

