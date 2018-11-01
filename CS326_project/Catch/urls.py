from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url


urlpatterns = [
    path('homePage', views.home, name = "homePage"),
    path('eventsPage', views.events, name = "eventsPage"),
    path('mapPage', views.map, name = "mapPage"),
    path('profilePage', views.profile, name = "profilePage"),
    path('aboutPage', views.about, name = "aboutPage"),
    path('add', views.EventCreate.as_view(success_url='homePage'), name='Event-add'),
    path('addPet', views.PetCreate.as_view(success_url='profilePage'), name='Pet-add'),
    # path('add/$', views.EventCreate.as_view(success_url='homePage.html'), name='Event-add'),
    # path('navbar', views.navbar, name = "navbar"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
