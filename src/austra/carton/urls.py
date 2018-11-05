from django.urls import path
from django.conf.urls import include, url
from carton import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name = "index"),
    path('calendar/', views.calendar, name = "calendar")

]
