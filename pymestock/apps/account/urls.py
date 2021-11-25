from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("signup", views.register_user, name="signup"),
    path("login", views.login_user, name="login"),
    path("logout", views.logout_user, name="logout"),
    path("error", views.error, name="error"),
    path("dashboard", views.dashboard, name="dashboard")
]
