from django.urls import path, include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
    path('edit/<int:id>/', views.edit_student, name='edit_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
    path('register/' , views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('api/students/', views.student_api),
    path('api/students/<int:id>/', views.student_detail_api),
    path('dashboard/' , views.dashboard, name='dashboard'),

] +static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)