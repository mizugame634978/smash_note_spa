
from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('smash_note/',include('smash_note.urls')),#smash_noteのurlだとsmash_noteに飛ぶ
    path('',RedirectView.as_view(url = '/smash_note/')),#urlになにもないとsmash_noteにurlがなる
]
