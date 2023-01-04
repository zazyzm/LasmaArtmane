from django.shortcuts import render
from helpers.navbar.context import navigation_sections
from picture.models import Picture


def index(request):
    main_pic = Picture.objects.filter(name='main')

    context = {
        'sections': navigation_sections(),
        'main_pic': main_pic[0]
    }
    return render(request, 'pages/index.html', context)
