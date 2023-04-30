from django.urls import reverse_lazy
from django.views import generic
from .models import Character,MatchResult
from .forms import MatchResultForm

from django.contrib.auth.mixins import LoginRequiredMixin#アクセス制御
#Create your views here.
class CharacterSelect(generic.ListView):
    model = Character#表示させるなら横６スマホ？pc１０？
class CharacterDetailView(generic.DetailView):
    model = Character#テンプレート名を省略しているので、Character_detail.htmlが対応される
'''
class CharacterDetailView(generic.DetailView):
    model = Character
    template_name = 'character_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = MatchResult.objects.filter(player_character_id=self.object.id)
        return context
'''
class MemoCreateView(LoginRequiredMixin,generic.edit.CreateView):
    model=MatchResult

    #template_name = 'smash_note/character_detail.html'
    #fields= '__all__'
    fields = ['player_character_id','opponent_character_id','win_flag','memo']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super(MemoCreateView,self).form_valid(form)


class MemoUpdateView(generic.UpdateView):
    model = Character
    fields= '__all__'
