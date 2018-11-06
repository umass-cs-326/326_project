from django.urls import path
from django.conf.urls import include, url
from carton import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name = "index"),
    path('calendar/', views.calendar, name = "calendar"),
    path('instructors/', views.InstructorListView.as_view(), name="instructors"),
    path('instructor/<int:pk>', views.InstructorDetailView.as_view(), name="instructor-detail"),
    path('course/<int:pk>', views.CourseDetailView.as_view(), name="course-detail"),
    url(r'^comments/', include('django_comments.urls')),
]
