from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='places'),
    path('places/<int:place_id>/', views.place_detail, name='place_detail'),
]
