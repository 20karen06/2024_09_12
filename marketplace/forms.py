from django import forms
from .models import Animal, Rating, Feedback


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['animal_type', 'breed', 'character_description', 'age', 'sex', 'value', 'picture', 'is_purebred',
                  'is_neutered']


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating', 'comment']


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['message']
