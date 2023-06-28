from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # Main URL
    path("", views.index, name="index"),
    
    # Login URL
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    # Logout URL
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Registration URL
    # Add your own view or use Django's built-in RegistrationView

    # Additional authentication-related URLs (e.g., password reset)
    # Add any necessary password reset, password change, or account activation URLs

]