
from django.urls import path
from . import views

urlpatterns = [
    path('', views.sample_list, name='sample_list'),
    path('<int:pk>/', views.sample_detail, name='sample_detail'),
    path('create/', views.sample_create, name='sample_create'),
    path('<int:pk>/update/', views.sample_update, name='sample_update'),
    path('<int:pk>/delete/', views.sample_delete, name='sample_delete'),
]
