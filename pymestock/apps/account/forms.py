from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
)
from .models import User
from django.db import transaction


class UserSignInForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "Usuario",
                "id": "floatingInput",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password",
                "id": "floatingPassword",
            }
        )
    )


class UserSignUpForm(forms.ModelForm):
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_owner = True
        user.save()
