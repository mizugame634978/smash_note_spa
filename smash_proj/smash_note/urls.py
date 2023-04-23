from django.urls import path
from .import views

from django.conf.urls.static import static
from django.conf import settings
app_name="smash_note"


urlpatterns = [
    path('',views.CharacterSelect.as_view(),name='character_list'),#name=によりhtml上でcharaという名前で呼び出せる

] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


