# pokemon_app/urls.py
from django.urls import path, register_converter
# Explicit imports
from .views import All_moves, A_move
urlpatterns = [
path("<str:name>/", A_move.as_view(), name="a_move"),
path("", All_moves.as_view(), name="all_moves"),
]