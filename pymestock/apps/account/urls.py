from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

from pymestock.apps.account.forms import UserLoginForm

from .views import OwnerSignUpView, WorkerSignUpView

urlpatterns = [
    path(
        "account/login/",
        auth_views.LoginView.as_view(
            template_name="account/login.html", form_class=UserLoginForm
        ),
        name="login",
    ),
    path("account/owner/signup", OwnerSignUpView.as_view(), name="owner-signup"),
    path("account/worker/signup", WorkerSignUpView.as_view(), name="worker-signup"),
    path("account/dashboard", views.dashboard, name = "dashboard")
    # TODO
    # path("account/profile/edit", views.edit, name = "edit_details"),
    # path("account/profile/delete-user", views.detele_user, name = "delete_user" ),
]
