
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('contact/',views.contact,name='contact'),

    path('eng',views.eng,name='eng'),
    path('cpp',views.cpp,name='cpp'),
    path('dsa',views.dsa,name='dsa')
    


]