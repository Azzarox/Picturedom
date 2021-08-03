from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Picturedom.views import raise_error_400_bad_request, raise_error_403_forbidden, raise_error_404_page_not_found, \
    raise_error_500_server_error

error_templates = [path('400/', raise_error_400_bad_request),
                   path('403/', raise_error_403_forbidden),
                   path('404/', raise_error_404_page_not_found),
                   path('500/', raise_error_500_server_error),
                   ]
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('django.contrib.auth.urls')),
                  path('', include('Picturedom.auth_app.urls')),
                  path('', include('Picturedom.profile_user.urls')),
                  path('', include('Picturedom.photo.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + error_templates

handler400 = 'Picturedom.views.error_400_view'
handler403 = 'Picturedom.views.error_403_view'
handler404 = 'Picturedom.views.error_404_view'
handler500 = 'Picturedom.views.error_500_view'
