from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'payments'

urlpatterns = [
    # Main URL
    path("", views.index, name="index"),
]