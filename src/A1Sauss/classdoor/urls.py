from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("class/", views.classpage, name="classpage"),
    path("feed/", views.feed, name="feed"),
    path("login/", views.login, name="login"),
    path("profile/", views.profile, name="profile"),
    path("review/", views.review, name="review"),
]