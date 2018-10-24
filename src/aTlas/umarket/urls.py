from django.urls import path
from umarket import views


urlpatterns = [
    path('', name="home_page"),
    path('products/', views.ProductBrowsing.as_view(), name="product-browsing"),
    path('products/<int:pk>', views.ProductDetailView.as_view(), name="product-detail"),
    path('user/<int:pk', views.UserDetailView.as_view(), name="user-detail"),
]
