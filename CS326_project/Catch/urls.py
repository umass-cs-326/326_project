from django.conf.urls import url
from django.views.generic.base import RedirectView
from Catch import views

urlpatterns = [
    url('homePage', views.home),
    url('aboutPage', views.about),
    url('')
]
