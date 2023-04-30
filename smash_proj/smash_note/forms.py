#from django.db import models
from django import forms
from .models import MatchResult
class MatchResultForm(forms.ModelForm):

    class Meta:

        model = MatchResult
        fields = ("player_character_id",'opponent_character_id',"author")
