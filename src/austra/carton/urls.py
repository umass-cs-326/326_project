from django.urls import path
from django.conf.urls import include, url
from carton import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name = "index"),
    # path('accounts/profile/', TemplateView.as_view(template_name="accounts/profile.html"), name = "profile"),
    path('accounts/profile/', views.profile_page, name = "profile"),
    path('calendar/', views.calendar, name = "calendar"),
    path('instructors/', views.InstructorListView.as_view(), name="instructors"),
    path('instructor/<int:pk>', views.InstructorDetailView.as_view(), name="instructor-detail"),
    path('course/<int:pk>', views.CourseDetailView.as_view(), name="course-detail"),
]
#Form pages
urlpatterns += [
    path('instructor/create/', views.InstructorCreate.as_view(), name='instructor-new'),
    path('course/create/', views.CourseCreate.as_view(), name='course-new'),
]
#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
