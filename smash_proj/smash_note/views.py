from django.urls import reverse_lazy
from django.views import generic
#from django.views.generic.edit import CreateView
from .models import Character,MatchResult
from .forms import MatchResultForm
from django.shortcuts import get_object_or_404 # get_object_or_404をインポート

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
        context['match_results'] = MatchResult.objects.filter(author=self.request.user)#ログインユーザーがauthorかどうかでフィルターをかけてる
        #print(context)
        return context
'''
class CharacterDetailView(generic.DetailView):
    model = Character
    template_name = 'character_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = MatchResult.objects.filter(player_character_id=self.obaa.id)
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


class MemoCreateView2(generic.edit.CreateView): # MemoCreateViewを定義し、CreateViewを継承する
    model = MatchResult # モデルにMatchResultを指定
    fields = ['player_character_id','win_flag', 'memo'] # フォームのフィールドにwin_flagとmemoを指定
    template_name = 'smash_note/MatchResult_form.html' # テンプレートの名前を指定

    # def get_form_kwargs(self): # フォームにキーワード引数を追加するためのメソッド
    #     kwargs = super().get_form_kwargs() # 親クラスのメソッドを呼び出し、返されたキーワード引数をkwargsに代入
    #     print("hoge")
    #     print(kwargs)
    #     print("hoge")
    #     #kwargs['instance'] = MatchResult(player_character_id= get_object_or_404(Character, pk=self.kwargs['pk']))
    #     #kwargs['author'] = self.request.user
    #     #kwargs['opponent_character_id'] = get_object_or_404(Character, pk=self.kwargs['pk'])

    #     #form.instance.author = self.request.user
    #     #kwargs['author'] = self.request.user # ログインユーザーをauthorに追加
    #     #kwargs['opponent_character_id'] = get_object_or_404(Character, pk=self.kwargs['pk']) # urlのpkからキャラクターを取得し、opponent_character_idに追加
    #     return kwargs # kwargsを返す

    def form_valid(self, form): # フォームが妥当かどうかを検証するためのメソッド
        form.instance.author = self.request.user # ログインユーザーをauthorに追加
        form.instance.opponent_character_id = get_object_or_404(Character, pk=self.kwargs['pk']) # urlのpkからキャラクターを取得し、player_character_idに追加
        return super().form_valid(form) # 親クラスのメソッドを呼び出し、返り値を返す

class MemoUpdateView(generic.UpdateView):
    model = Character
    fields= '__all__'
