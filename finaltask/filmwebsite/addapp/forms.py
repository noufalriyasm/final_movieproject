from django import forms
from filmapp.models import Category,Movie

class MovieForm(forms.ModelForm):
    category=forms.ModelChoiceField(queryset=Category.objects.all())
    image=forms.ImageField()
    slug=forms.SlugField()

    class Meta:
        model=Movie
        fields=['name','slug','description','category','actors','link','image','added_by']
