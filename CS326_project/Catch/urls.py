from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.conf.urls import include
from django.contrib.auth.decorators import login_required


urlpatterns = [
    # path('', views.home, name = "homePage"),
    path('homePage', views.home, name = "homePage"),
    path('eventsPage', views.UserViewEvents.as_view(), name = "eventsPage"),


    path('mapPage', views.map, name = "mapPage"),
    path('profilePage', views.UserViewProfileView.as_view(), name='profilePage'),

    # path('aboutPage', views.about, name = "aboutPage"),
    path('petPage', views.UserViewPets.as_view(), name = "petPage"),

    path('addEvent', views.EventCreate.as_view(success_url='homePage'), name='Event-add'),
    path('addPet', views.PetCreate.as_view(), name='Pet-add'),
    # path('add/$', views.EventCreate.as_view(success_url='homePage.html'), name='Event-add'),
    # path('navbar', views.navbar, name = "navbar"),

    path('accounts/signup', views.UserSignUpView.as_view(), name='user-sign-up'),
    path('account/edit', views.UserEditProfileView.as_view(), name='user-edit-profile'),
    path('account/view', views.UserViewProfileView.as_view(), name='user-view-profile'),
    path('account/login', views.UserViewProfileView.as_view(), name='user-view-profile'),
    #path('profile/edit', views.edit_profile, name='edit_profile')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
