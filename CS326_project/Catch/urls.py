from django.conf.urls import url
from django.views.generic.base import RedirectView
from Catch import views

urlpatterns = [
    url('homePage', views.home),
    url('eventsPage', views.events),
    url('mapPage', views.map),
    url('profilePage', views.profile),
    url('aboutPage', views.about),
    url('navbar', views.navbar),

]
