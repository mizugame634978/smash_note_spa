from django.contrib import admin

# ここに追加したものがadminでログインしたときにいじれる
from .models import Character, FavoriteCharacter, MatchResult

admin.site.register(Character)
#admin.site.register(User)
admin.site.register(MatchResult)
admin.site.register(FavoriteCharacter)
