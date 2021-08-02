from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Picturedom.photo.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', include('Picturedom.auth_app.urls')),
]
