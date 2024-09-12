from django.urls import path
from contact.views import *
urlpatterns = [
    path("", contact, name="contact.index" ),
]
