from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import RevisionNote


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("An account already uses this email.")
        return email


class RevisionNoteForm(forms.ModelForm):
    class Meta:
        model = RevisionNote
        fields = ("title", "subject", "content", "attachment")
        widgets = {
            "content": forms.Textarea(attrs={"rows": 10}),
        }

    def clean_attachment(self):
        attachment = self.cleaned_data.get("attachment")
        if attachment and attachment.size > 5 * 1024 * 1024:
            raise forms.ValidationError(
                "The uploaded file must be 5 MB or smaller."
            )
        return attachment
