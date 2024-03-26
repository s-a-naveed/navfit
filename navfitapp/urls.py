from django.urls import path
from navfitapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('plans/', views.plans, name='plans'),
    path('contactus/', views.contactus, name='contactus'),
    path('register/', views.registerpage, name='register'),
    path('login/',views.loginpage, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
]
