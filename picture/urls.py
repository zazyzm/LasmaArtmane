from django.urls import path
from . import views

urlpatterns = [
    path('<int:picture_id>', views.picture, name='picture'),
]
