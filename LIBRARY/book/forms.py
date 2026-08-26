from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_select2.forms import ModelSelect2MultipleWidget
from .models import Book, Author


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "genre", "publish_date", "pages", "price", "authors"]
        widgets = {
            "publish_date": forms.DateInput(attrs={"type": "date"}),
            "authors": ModelSelect2MultipleWidget(
                model=Author,
                search_fields=["first_name__icontains", "last_name__icontains"],
                attrs={
                    "data-placeholder": "search a author",
                    "style": "width: 100%;",
                },
            ),
        }
