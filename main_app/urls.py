from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('brands/', views.brands_index, name='index'),
    path('brands/<int:brand_id>/', views.brands_detail, name='detail'),
]
