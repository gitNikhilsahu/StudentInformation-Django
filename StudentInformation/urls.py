from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('contact/', views.contactView, name='contact'),
    path('about/', views.aboutView, name='about'),
    path('account/', include('Account.urls')),
    path('admin/', admin.site.urls),
]
