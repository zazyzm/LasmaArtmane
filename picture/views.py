from django.shortcuts import render, get_object_or_404

from helpers.navbar.context import navigation_sections
from picture.models import Picture


def picture(request, picture_id):
    picture_chosen = get_object_or_404(Picture, id=picture_id)
    context = {
        'sections': navigation_sections(),
        'picture': picture_chosen,
    }
    return render(request, 'pages/about.html', context)
