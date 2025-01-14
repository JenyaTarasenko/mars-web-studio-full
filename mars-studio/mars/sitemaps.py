from django.contrib.sitemaps import Sitemap
from .models import WebSait
from django.urls import reverse
from django.conf import settings

class WebsaiSitemap(Sitemap):
    changefreq = "weekly"  # Частота изменения страниц
    priority = 0.5         # Приоритет страниц
    
    def items(self):
        return WebSait.objects.all()
    
    def lastmode(self, obj):
        return obj.slug
    
    
    
    def get_absolute_url(self, obj):
        return reverse('mars:websait_detail', args=[obj.slug])
    
    def location(self, obj):
        return f"{settings.SITE_URL}/mars_studio/{obj.slug}/"
    
    # добавить после обновления домен