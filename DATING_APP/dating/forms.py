from django import forms
from .models import InterestNames

class InterestSelectionForm(forms.Form):
    # print(InterestNames.objects)
    interest = forms.ChoiceField(choices=(("Music", "Music"), ("Books", "Books"), ("Movies", "Movies"), ("Anime", "Anime")))

    