from django.urls import path
from django.conf.urls import include, url
from carton import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name = "index"),
#    path('registration/login/', TemplateView.as_view(template_name="registration/login.html"), name = "login"),
#    path('registration/logout/', TemplateView.as_view(template_name="registration/logout.html"), name = "logout"),
    path('tree/', TemplateView.as_view(template_name="tree.html"), name = "tree"),
    path('accounts/profile/', TemplateView.as_view(template_name="accounts/profile.html"), name = "profile"),
    path('calendar/', views.calendar, name = "calendar"),
    path('instructors/', views.InstructorListView.as_view(), name="instructors"),
    path('instructor/<int:pk>', views.InstructorDetailView.as_view(), name="instructor-detail"),
    path('course/<int:pk>', views.CourseDetailView.as_view(), name="course-detail"),
]
#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
