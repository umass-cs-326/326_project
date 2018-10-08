from django.conf.urls import url
from django.views.generic.base import RedirectView
from Catch import views


urlpatterns = [
    url('homePage', views.home, name = 'homePage'),
    url('formPage', views.form, name = 'formPage'),
    url('eventsPage', views.events, name = 'eventsPage'),
    url('profilePage', views.profile, name = 'profilePage'),
    url('mapPage', views.map, name = 'mapPage'),
    url('aboutPage', views.about, name = 'aboutPage'),
    url('add/$', views.EventsCreate.as_view(), name='Events-add')
    # url('navbar', views.navbar),
]
