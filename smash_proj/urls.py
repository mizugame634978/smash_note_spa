
from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView

from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('smash_note/',include('smash_note.urls')),#smash_noteのurlだとsmash_noteに飛ぶ  そしてこれをコメントアウトしないとmigrationできない？
    path('',RedirectView.as_view(url = '/smash_note/')),#urlになにもないとsmash_noteにurlがなる
    path('accounts/',include('accounts.urls')),# accounts.urls.pyを読み込むための設定を追加
    path('social-auth/', include('allauth.urls')),
    #http://127.0.0.1:8000/social-auth/google/login/?next=/
]# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#画像を表示させる時に使うやつ
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
