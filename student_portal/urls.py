from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.portal_home, name='portal_home'),
    path('students/<int:pk>/', views.portal_detail, name='portal_detail'),
    
    path('admin-login/', views.admin_login, name='admin_login'),
    path('dashboard/', views.dashboard, name='portal_dashboard'),
    path('logout/', views.admin_logout, name='portal_logout'),
    path('my-profile/', views.student_profile, name='student_profile'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
