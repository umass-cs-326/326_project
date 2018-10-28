from django.urls import path
from . import views
urlpatterns = [
    path('homePage', views.home, name = "homePage"),
    path('eventsPage', views.events, name = "eventsPage"),
    path('mapPage', views.map, name = "mapPage"),
    path('profilePage', views.profile, name = "profilePage"),
    path('aboutPage', views.about, name = "aboutPage"),
    # path('navbar', views.navbar, name = "navbar"),
]
