
from django.urls import path

from aensongaApp.views import (about, blog, causes, contact, donate, event, index, service, 
                               single, team, volunteer, become_volunteer, contact_us, donate_view, verify_donation )

urlpatterns = [
    path('about/', about, name="about"),
    path('blog/', blog, name="blog"),
    path('causes/', causes, name="causes"),
    path('contact/', contact, name="contact"),
    path('donate/', donate, name="donate"),
    path('event/', event, name="event"),
    path('', index, name="index"),
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