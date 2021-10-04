from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views
from .forms import UserSignInForm

urlpatterns = [
    path("account/", include("django.contrib.auth.urls")),
    path(
        "account/signin",
        auth_views.LoginView.as_view(
            template_name="account/signin.html", form_class=UserSignInForm
        ),
        name="signin",
    ),
    path("account/signup", views.UserSignUpView.as_view, name="signup"),
    path(
        "account/signout",
        auth_views.LogoutView.as_view(next_page="/account/signout/"),
        name="signout",
    ),
    # TODO
    # path("account/dashboard", views.dashboard, name = "dashboard"),
    # path("account/profile/edit", views.edit, name = "edit_details"),
    # path("account/profile/delete-user", views.detele_user, name = "delete_user" ),
]
