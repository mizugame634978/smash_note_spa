from django.urls import reverse_lazy
from django.views import generic
#from django.views.generic.edit import CreateView
from .models import Character,MatchResult,FavoriteCharacter
from .forms import MatchResultForm
from django.shortcuts import get_object_or_404 # get_object_or_404をインポート
from django.contrib.auth.mixins import LoginRequiredMixin#アクセス制御
from django.core.exceptions import PermissionDenied#Updateで使う

from django.shortcuts import render,redirect
from django.http import HttpResponse

from .forms import CharacterSelectForm

from django.contrib.auth.mixins import LoginRequiredMixin#アクセス制御

from django.shortcuts import render
from django.views import View
from .models import FavoriteCharacter
from .forms import FavoriteCharacterForm

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


        #↓これでhtml上でmatch_resultsとかけばmatch_resultsを呼び出せる
        #context['match_results'] = MatchResult.objects.filter(author=self.request.user)#authorが現在のログインユーザーであるオブジェクトのみをフィルタリングしています
        character = self.object
        match_results =  MatchResult.objects.filter(author=self.request.user)
        match_results = match_results.filter(opponent_character_id=character.id)#opponent_character_idで絞り込み
        print(character.id)
        filter_id = self.request.GET.get('filter')
        print(filter_id,'フィルターid')

        if filter_id:
            match_results = match_results.filter(player_character_id=filter_id)
        context['match_results'] = match_results

        if filter_id:
            filtered_character = Character.objects.get(id=filter_id)
        else:
            filtered_character = None
        context['filter_character'] = filtered_character

        wins = match_results.filter(opponent_character_id=character, win_flag=True).count()
        losses = match_results.filter(opponent_character_id=character, win_flag=False).count()
        total_matches = match_results.count()
        nocon = total_matches-wins-losses

        if( (wins+losses) ==0):
            win_rate = '?'#勝ちも負けも記録されていないとき勝率を？にする
        elif(wins == 0 ):
            win_rate=0#0除算回避
        else:
            win_rate = round(wins / (wins+losses) * 100) #if (wins+losses) != 0 else 0
        context['wins'] = wins
        context['losses'] = losses
        context['total_matches'] = total_matches
        context['win_rate'] = win_rate
        context['nocon']=nocon
        print("--get_context_data--")

        character = Character.objects.all()
        context['characters'] = character
        if self.request.user.is_authenticated:
            try:
                favorite_characters = FavoriteCharacter.objects.get(user=self.request.user)
                context['favorite_characters'] = favorite_characters.characters.all()
            except FavoriteCharacter.DoesNotExist:
                pass
        return context
def filter_view(request):
    print("def")
    filter_id = request.GET.get('filter')
    if filter_id:
        filtered_character = Character.objects.get(id=filter_id)
        filtered_models = MatchResult.objects.filter(player_character_id=filter_id)
    else:
        filtered_models = MatchResult.objects.all()
        filtered_character = None
    context = {'models': filtered_models, 'filter_character': filtered_character}
    return render(request, 'smash_note/character_detail.html', context)


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




def get_character_stats(character):
    matches_as_opponent = MatchResult.objects.filter(opponent_character_id=character.id)
    total_matches = matches_as_opponent.count() + MatchResult.objects.filter(player_character_id=character.id).count()
    wins_as_player = MatchResult.objects.filter(player_character_id=character, win_flag=True).count()
    win_rate = wins_as_player / total_matches * 100 if total_matches > 0 else 0
    stats = {'total_matches': total_matches, 'wins': wins_as_player, 'win_rate': win_rate}
    #return stats
    return HttpResponse(matches_as_opponent)



class FavoriteCharactersView(View):
    def get(self, request):
        form = FavoriteCharacterForm()
        character_choices = Character.objects.all
        favorite_character = request.user.favoritecharacter
        print("c")
        print(favorite_character)
        if self.request.user.is_authenticated:
            try:
                favorite_characters = FavoriteCharacter.objects.get(user=self.request.user)
                favorite_characters = favorite_characters.characters.all()
                print("deb")
                print(favorite_characters)
                return render(request, 'smash_note/favorite_characters.html', {'form': form, 'character_choices': character_choices,'favorite_character':favorite_character,'favorite_characters':favorite_characters})
            except FavoriteCharacter.DoesNotExist:
                pass
        return render(request, 'smash_note/favorite_characters.html', {'form': form, 'character_choices': character_choices,'favorite_character':favorite_character})

    def post(self, request):
        form = FavoriteCharacterForm(request.POST)
        character_choices = Character.objects.all
        if form.is_valid():
            character_id = form.cleaned_data['characters']
            selected_chara_id = request.POST.get('characters')
            print("aa",selected_chara_id)

            print(character_id)
            favorite_character = request.user.favoritecharacter
            favorite_character.characters.add(selected_chara_id)
            print("a")
            #return redirect('smash_note/character_list.html')
            #return reverse_lazy("smash_note:favorite_character")
        print("b")
        try:
            favorite_characters = FavoriteCharacter.objects.get(user=self.request.user)
            favorite_characters = favorite_characters.characters.all()
            print("deb")
            print(favorite_characters)
            return render(request, 'smash_note/favorite_characters.html', {'form': form, 'character_choices': character_choices,'favorite_character':favorite_character,'favorite_characters':favorite_characters})
        except FavoriteCharacter.DoesNotExist:
            pass
        return render(request, 'smash_note/favorite_characters.html', {'form': form,'character_choices': character_choices,'favorite_character':favorite_character})
#'''
class FavoriteDeleteView(generic.DeleteView):


    print("c")


    template_name = 'smash_note/matchresult_confirm_delete.html'
    model = FavoriteCharacter
    #template_name = 'smash_note/favorite_character.html'
    #success_url = reverse_lazy('smash_note:character_index')
    #success_url = reverse_lazy('smash_note:character_detail')
    def get_success_url(self):
        #return reverse_lazy('smash_note:character_detail', kwargs={'pk': self.object.pk})
        #print("\n" ,self,"\n")
        return reverse_lazy('smash_note/favorite_character.html')
        pass
'''
class FavoriteDeleteView(View):
    print("a")
    template_name = 'smash_note/matchresult_confirm_delete.html'
    def post(self, request, character_id, *args, **kwargs):
        favorite_character = get_object_or_404(FavoriteCharacter, user=request.user)
        favorite_character.characters.remove(character_id)
        favorite_character.save()
        return redirect('favorite_characters')  # 削除後にリダイレクトするURLを設定してください
    # def post(self, request, *args, **kwargs):
    #     #character_id = request.POST.get('character_id')  # フォームからキャラクターIDを取得
    #     favorite_character = get_object_or_404(FavoriteCharacter, user=request.user)
    #     print(favorite_character)
    #     #favorite_character.characters.remove(character_id)
    #     favorite_character.save()
    #     return redirect('smash_note/favorite_character.html')  # 削除後にリダイレクトするURLを設定してください

'''
