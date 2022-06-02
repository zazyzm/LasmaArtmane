from django.urls import path
from . import views


urlpatterns = [
    path('<gallery_name>', views.gallery, name='gallery')
]
