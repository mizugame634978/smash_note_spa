from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
# from rest_framework import DefaultRouter
# from CharacterViewSet import views
from  . import views
app_name = "smash_note"


urlpatterns = [
#     path("", views.CharacterSelect.as_view(), name="character_index"),  # name=によりhtml上でcharaという名前で呼び出せる
#     path("<int:pk>/", views.CharacterDetailView.as_view(), name="character_detail"),
#     path("<int:pk>/create/", views.MemoCreateView.as_view(), name="memo_create"),
#     # path('create/',views.MemoCreateView.as_view(),name='memo_create'),
#     path("<int:pk>/update/", views.MemoUpdateView.as_view(), name="memo_update"),
#     path("<int:pk>/delete/", views.MemoDeleteView.as_view(), name="memo_delete"),
#     # path('<int:pk>/update/<int:pk>',views.MemoUpdateView.as_view(),name='memo_update'),
#     path("favorite-characters/", views.FavoriteCharactersView.as_view(), name="favorite_characters"),
#     path("<int:pk>/fcdelete/", views.FavoriteDeleteView.as_view(), name="fc_delete"),
#     path("tool/", views.ToolView.as_view(), name="tool"),
#     path("userate/", views.UseRateView.as_view(), name="use_rate"),
#     path("winrate/", views.WinRateView.as_view(), name="win_rate"),
    path("api/",views.api_character_list),
]
# router = DefaultRouter()
# router.register(r'api/', CharacterViewSet)

# urlpatterns = router.urls