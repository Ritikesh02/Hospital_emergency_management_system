from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from emergency.views import home_view  # Import home_view

def home(request):
    if request.user.is_authenticated:
        return HttpResponse("""
            <h1>Welcome to the Medical Emergency System</h1>
            <a href="/emergency/request-help/">Request Help</a>
        """)
    else:
        return HttpResponse("""
            <h1>Welcome to the Medical Emergency System</h1>
            <a href="/users/register/">Register</a>
            <a href="/login/">Login</a>
        """)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # This makes sure clicking 'Home' loads the correct page
    path('users/', include('users.urls')),
    path('emergency/', include('emergency.urls')),
    path('medical_records/', include('medical_records.urls')),
    path('chat/', include('chat.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
