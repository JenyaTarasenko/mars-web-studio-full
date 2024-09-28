from django.contrib import admin
from .models import WebSait, Contact

@admin.register(WebSait)
class WebSaitAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description', 'link']
    search_fields = ('name', 'description')  # Поиск по имени и описанию
    prepopulated_fields = {'slug': ('name',)}
    
    
     
    
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_dispplay = ['name', 'phone_number']
    