from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('umarket/', include('umarket.urls')),
    path('', RedirectView.as_view(url='/umarket/', permanent=True)),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
