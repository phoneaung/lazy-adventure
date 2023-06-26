from django.conf import settings
from django.conf.urls.static import static  
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include

from core.views import index, about
from userprofile.views import signup

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', include('dashboard.urls')),
    path('dashboard/candidates/', include('candidate.urls')),
    path('about/', about, name='about'),
    path('sign-up/', signup, name='signup'),
    path('log-in/', views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('log-out', views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
