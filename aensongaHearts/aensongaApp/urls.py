
from django.urls import path

from aensongaApp.views import (about, blog, causes, contact, donate, event, index, projects, service, 
                               single, team, volunteer, become_volunteer, contact_us, donate_view, verify_donation )

urlpatterns = [
    path('about/', about, name="about"),
    path('blog/', blog, name="blog"),
    path('causes/', causes, name="causes"),
    path('contact/', contact, name="contact"),
    path('donate/', donate, name="donate"),
    path('event/', event, name="event"),
    path('', index, name="index"),
    path('projects/', projects, name="projects"),
    path('service/', service, name="service"),
    path('gallary/<str:project_name>/', single, name="single"),
    # path('team/', team, name="team"),
    path('volunteer/', volunteer, name="volunteer"),
    
    #form actions
    path('become_volunteer/', become_volunteer, name="become_volunteer"),
    path('contact_us/', contact_us, name="contact_us"),
    path('donate_view/', donate_view, name="donate_view"),
    path('verify_donation/<str:ref>/', verify_donation, name="verify_donation"),
]



# import os
# import sys

# # add your project directory to the sys.path
# project_home = '/home/aensongahearts/aensongaHearts'
# if project_home not in sys.path:
#     sys.path.insert(0, project_home)

# # set environment variable to tell django where your settings.py is
# os.environ['DJANGO_SETTINGS_MODULE'] = 'aensongaHearts.settings'


# # serve django via WSGI
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()
