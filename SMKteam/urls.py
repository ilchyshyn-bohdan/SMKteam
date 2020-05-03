from django.contrib import admin
from django.urls import path, include

from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('anycluster/', include('anycluster.urls')),
    path('models/', include('models.urls')),
]
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)