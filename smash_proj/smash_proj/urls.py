
from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView

from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('smash_note/',include('smash_note.urls')),#smash_noteのurlだとsmash_noteに飛ぶ
    path('',RedirectView.as_view(url = '/smash_note/')),#urlになにもないとsmash_noteにurlがなる
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#画像を表示させる時に使うやつ
