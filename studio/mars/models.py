from django.db import models
from django.urls import reverse


class WebSait(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='web-site/%Y/%m/%d', blank=True)
    link = models.URLField()
    created = models.DateTimeField(auto_now_add=True)  # Автоматически добавляет дату создания записи
    updated = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created'])
        ]
        
    def __str__(self):
        return self.name 
    
    def get_absolute_url(self):
        return reverse("websait_detail", kwargs={"slug": self.slug})
    
        
        
        
class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.name}-{self.phone_number}"