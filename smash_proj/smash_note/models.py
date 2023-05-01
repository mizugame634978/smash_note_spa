from django.db import models
from django.urls import reverse


class Character(models.Model):
    #character_id = models.IntegerField#djangoがidという名前で定義してくれるので不要？
    character_name = models.CharField(max_length=255)
    image_url = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.character_name#このクラス名で呼び出されたときにreturnのコードを実行



'''
    models.ForeignKeyの第一引数には、関連するモデルのクラス名を指定する必要があります。例えば、models.ForeignKey(Character)と書くことで、
    Characterモデルと関連付けることができます。この場合、player_character_idフィールドはCharacterのインスタンスを参照することができます。

    Characterモデルにはidという名前の自動生成されたプライマリーキーがありますが、models.ForeignKeyにCharacterを渡すことで、
    そのプライマリーキーと紐づけることができます。つまり、player_character_idは、Characterモデルのプライマリーキーであるidを
    参照することになります。↓
    '''
class MatchResult(models.Model):#djangoだとキャメルケースで書く
    player_character_id = models.ForeignKey(Character,related_name='player_character',on_delete=models.CASCADE)
    opponent_character_id = models.ForeignKey(Character,related_name='opponent_character',on_delete=models.CASCADE)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )

    win_flag = models.BooleanField()
    memo = models.TextField(max_length=3000)
    memo_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return str(self.id)
    def get_absolute_url(self):
        #return reverse("smash_note:character_detail", kwargs={"pk": self.pk})#urlからリダイレクト先のurlを調べる
        return reverse("smash_note:character_detail", kwargs={"pk": self.opponent_character_id.pk})#urlからリダイレクト  つまり呼び出したと似にopponent_character_idのurlに飛ぶ


