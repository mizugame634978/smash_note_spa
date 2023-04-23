from django.urls import path
from .import views
app_name="smash_note"

urlpatterns = [
    path('',views.CharacterSelect.as_view(),name='character'),#name=によりhtml上でcharaという名前で呼び出せる

]

