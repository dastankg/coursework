from django import forms

from .models import FaqFeedback


class FaqFeedbackForm(forms.ModelForm):
    class Meta:
        model = FaqFeedback
        fields = ('name', 'email',
                  'phone', 'title', 'message')

        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Name"}),
            'email': forms.TextInput(attrs={"class": "form-control", "placeholder": "Email"}),
            'phone': forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone"}),
            'title': forms.TextInput(attrs={"class": "form-control", "placeholder": "Subject"}),
            'message': forms.Textarea(attrs={"class": "form-control", "placeholder": "Your Message"}),
        }
        labels = {
            "name": '',
            "email": '',
            "phone": '',
            "title": '',
            "message": ''
        }
