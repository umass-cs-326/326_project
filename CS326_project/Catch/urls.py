from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('homePage', views.home, name = "homePage"),
    path('eventsPage', views.events, name = "eventsPage"),
    path('mapPage', views.map, name = "mapPage"),
    path('profilePage', views.profile, name = "profilePage"),
    path('aboutPage', views.about, name = "aboutPage"),
    # path('navbar', views.navbar, name = "navbar"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
