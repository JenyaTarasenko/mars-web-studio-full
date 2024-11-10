from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import TemplateView 


app_name = 'mars'

urlpatterns = [
    
    path('', views.submith_question, name="index"),#главная
    path('mars_studio/<slug:slug>/',views.DetailViewItem.as_view(), name='websait_detail'),#детальная информация
    path('about-mars-studio/',TemplateView.as_view(template_name="app/pages/about.html"), name='about'),#о нас без view
    path('etapy-raboti-mars/', TemplateView.as_view(template_name="app/pages/etapy.html"), name="etapy"),
    path('umovi-raboti-mars/', TemplateView.as_view(template_name="app/pages/umovi.html"), name="umovi"),
    path('perezapusk-saita-mars/', TemplateView.as_view(template_name="app/pages/zapusk-saita.html"), name="zapusk"),
   
]
