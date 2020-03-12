from django.urls import path
from . import views

urlpatterns = [
    path('', views.accountHome, name='account-home'),
    path('register/', views.registerView, name='register'),
    path('login/', views.loginView, name='login'),
    
    path('student/', views.studentView, name='student'),
    path('admin/', views.adminView, name='admin'),

    path('view_profile/', views.studentViewProfile),
    path('update_profile/', views.studentUpdateProfile),

]