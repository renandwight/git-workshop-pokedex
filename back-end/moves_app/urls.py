from django.urls import path
from .views import A_move, All_moves

urlpatterns = [
    path("<str:name>/", A_move.as_view(), name="a_move"),
    path("", All_moves.as_view(), name="all_moves"),
]

