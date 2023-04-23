from django.urls import reverse_lazy
from django.views import generic
from .models import Character,User,MatchResult

#Create your views here.
class CharacterSelect(generic.ListView):
    model = Character#表示させるなら横６スマホ？pc１０？


