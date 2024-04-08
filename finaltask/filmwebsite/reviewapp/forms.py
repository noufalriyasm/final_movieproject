from django import forms
from .models import Rating,Review


class RatingForm(forms.ModelForm):
    class Meta:
        model=Rating
        fields=['rating']

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=['text']