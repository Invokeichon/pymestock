from django.views.generic import CreateView
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .forms import OwnerSignUpForm, WorkerSignUpForm
from .models import User
from ...decorators import owner_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class OwnerSignUpView(CreateView):
    model = User
    form_class = OwnerSignUpForm
    template_name = "account/signup.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "owner"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("pymestock:index")


@method_decorator(login_required, name="dispatch")
@method_decorator(owner_required, name="dispatch")
class WorkerSignUpView(CreateView):
    model = User
    form_class = WorkerSignUpForm
    template_name = "account/worker/signup.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "worker"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("pymestock:index")
