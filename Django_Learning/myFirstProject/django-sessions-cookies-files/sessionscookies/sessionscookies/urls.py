from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('app_cookies/', include('app_cookies.urls')),
    path('app_sessions/', include('app_sessions.urls')),
    path('admin/', admin.site.urls),
]
