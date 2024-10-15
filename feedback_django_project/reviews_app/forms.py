from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(
        label="Your Name", max_length=50, required=True, error_messages={
            "required": "Your name must not be empty",
            "max_length": "Your name cannot be longer than 50 characters."
        })
