from django.urls import path, include
from . import views
urlpatterns = [
    path("",views.home, name = 'home'),
    path("projects/",views.projects, name = 'projects'), 
    path("resume/", views.resume, name='resume'), 
    path("contact/", views.contact, name='contact'), 
    path("gallery/", views.gallery, name='gallery'),  # Include the URLs from the gallery app
]