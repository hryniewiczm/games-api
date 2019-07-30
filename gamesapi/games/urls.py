from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('games/', views.game_list, name='games_list'),
    path('game/<int:pk>/', views.game_detail, name='game_detail')
]
