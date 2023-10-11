
from django.urls import path

from aensongaApp.views import (about, blog, causes, contact, donate, event, index, service, single)

urlpatterns = [
    path('about/', about, name="about"),
    path('blog/', blog, name="blog"),
    path('causes/', causes, name="causes"),
    path('contact/', contact, name="contact"),
    path('donate/', donate, name="donate"),
    path('event/', event, name="event"),
    path('', index, name="index"),
    path('service/', service, name="service"),
    path('single/', single, name="single"),
]