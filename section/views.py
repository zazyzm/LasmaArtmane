from django.shortcuts import render

from gallery.models import Gallery
from helpers.navbar.context import navigation_sections
from section.models import Section
from picture.models import Picture
import pandas
import json


def index(request):
    main_pic = Picture.objects.filter(name='main')

    context = {
        'sections': navigation_sections(),
        'main_pic': main_pic[0]
    }
    return render(request, 'pages/index.html', context)
    # <div class="tab">
    #     {% for section in sections %}
    #     <button class="tablinks">{{ section.name }}</button>
    #     {% endfor %}
    # </div>

# def index(request):
#     active_sections = Section.objects.filter(is_active=True).order_by('id')
#     active_galeries = Gallery.objects.values('name', 'section__name').filter(is_active=True).order_by('id')
#     context = {
#         'sections': active_sections,
#         'galleries': active_galeries,
#     }
#     # print('context:', context)
#     print('active_galeries:', active_galeries)
#     return render(request, 'pages/index.html', context)