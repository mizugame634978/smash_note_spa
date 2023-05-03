from django.urls import reverse_lazy
from django.views import generic
#from django.views.generic.edit import CreateView
from .models import Character,MatchResult
from .forms import MatchResultForm
from django.shortcuts import get_object_or_404 # get_object_or_404をインポート
from django.contrib.auth.mixins import LoginRequiredMixin#アクセス制御
from django.core.exceptions import PermissionDenied#Updateで使う

from django.contrib.auth.mixins import LoginRequiredMixin#アクセス制御
#Create your views here.
class CharacterSelect(generic.ListView):
    model = Character#表示させるなら横６スマホ？pc１０？
class CharacterDetailView(generic.DetailView):
    model = Character#テンプレート名を省略しているので、Character_detail.htmlが対応される
    template_name = 'smash_note/character_detail.html'
    # context_object_name = 'characters_detail'
    # queryset = Character.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(context)
        # print(" ")
        # print(" ")
        #context['match_results'] = MatchResult.objects.all()
        context['match_results'] = MatchResult.objects.filter(author=self.request.user)#authorが現在のログインユーザーであるオブジェクトのみをフィルタリングしています
        #print(context)
        return context

class MemoCreateView(LoginRequiredMixin,generic.edit.CreateView):
    model=MatchResult

    #template_name = 'smash_note/character_detail.html'
    #fields= '__all__'
    fields = ['player_character_id','opponent_character_id','win_flag','memo']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super(MemoCreateView,self).form_valid(form)


class MemoCreateView2(generic.CreateView): # MemoCreateViewを定義し、CreateViewを継承する
    model = MatchResult # モデルにMatchResultを指定
    fields = ['player_character_id','win_flag', 'memo'] # フォームのフィールドにwin_flagとmemoを指定
    template_name = 'smash_note/MatchResult_form.html' # テンプレートの名前を指定
    def form_valid(self, form): # フォームが妥当かどうかを検証するためのメソッド
        form.instance.author = self.request.user # ログインユーザーをauthorに追加
        form.instance.opponent_character_id = get_object_or_404(Character, pk=self.kwargs['pk']) # urlのpkからキャラクターを取得し、player_character_idに追加
        return super().form_valid(form) # 親クラスのメソッドを呼び出し、返り値を返す

class MemoUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = MatchResult

    fields=  ['player_character_id','win_flag','memo']

    def dispatch(self,request,*args,**kwargs):#dispatchメソッドをオーバーライド
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied("You do not have permission to edit.")
        return super(MemoUpdateView,self).dispatch(request,*args,**kwargs)

class MemoDeleteView(generic.DeleteView):
    model = MatchResult
    template_name = 'smash_note/matchresult_confirm_delete.html'
    #success_url = reverse_lazy('smash_note:character_index')
    #success_url = reverse_lazy('smash_note:character_detail')
    def get_success_url(self):
        #return reverse_lazy('smash_note:character_detail', kwargs={'pk': self.object.pk})
        #print("\n" ,self,"\n")
        return reverse_lazy('smash_note:character_detail', kwargs={'pk': self.object.opponent_character_id.pk})

