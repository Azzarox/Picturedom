from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', include('Picturedom.auth_app.urls')),
    path('', include('Picturedom.profile_user.urls')),
    path('', include('Picturedom.photo.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
