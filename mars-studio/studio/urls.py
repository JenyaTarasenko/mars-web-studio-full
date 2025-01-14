
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from mars.sitemaps import WebsaiSitemap
from django.contrib.sitemaps.views import sitemap


sitemaps = {
    'websait': WebsaiSitemap,  # Подключаем созданный Sitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),# Подключаем созданный Sitemap
    path('', include('mars.urls', namespace='mars')),#app_name
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
    
