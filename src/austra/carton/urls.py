from django.urls import path
from django.conf.urls import include, url
from carton import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name = "index"),
    path('login/', TemplateView.as_view(template_name="login.html"), name = "login"),
    path('tree/', TemplateView.as_view(template_name="tree.html"), name = "tree"),
    path('profile/', TemplateView.as_view(template_name="user_profile.html"), name = "profile"),
    path('calendar/', views.calendar, name = "calendar"),
    path('instructors/', views.InstructorListView.as_view(), name="instructors"),
    path('instructor/<int:pk>', views.InstructorDetailView.as_view(), name="instructor-detail"),
    path('course/<int:pk>', views.CourseDetailView.as_view(), name="course-detail"),
]
