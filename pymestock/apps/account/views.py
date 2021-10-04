from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth import login
from django.shortcuts import redirect

from .forms import UserSignUpForm
from .models import User

class UserSignUpView(CreateView):
    model = User
    form_class = UserSignUpForm
    template_name = "account/signup.html"

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('user:dashboard')
