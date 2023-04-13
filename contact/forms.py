from django import forms

from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('first_name', 'last_name', 'email',
                  'phone', 'title', 'message')

        widgets = {
            'first_name': forms.TextInput(attrs={"class": "form-control"}),
            'last_name': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.TextInput(attrs={"class": "form-control"}),
            'phone': forms.TextInput(attrs={"class": "form-control"}),
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'message': forms.Textarea(attrs={"class": "form-control"}),
        }
