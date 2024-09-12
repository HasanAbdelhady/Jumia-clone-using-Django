from django.urls import path
from aboutus.views import about
urlpatterns = [
    path("", about, name="about.index"),
]
