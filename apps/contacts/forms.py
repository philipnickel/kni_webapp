from django import forms
from .models import ContactSubmission


class ContactForm(forms.ModelForm):
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput)

    class Meta:
        model = ContactSubmission
        fields = ["name", "email", "phone", "message", "consent"]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 4})
        }

    def clean(self):
        data = super().clean()
        if data.get("honeypot"):
            raise forms.ValidationError("Spam detected.")
        return data

