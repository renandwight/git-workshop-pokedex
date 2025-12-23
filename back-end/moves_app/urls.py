
urlpatterns = [
path("<str:name>/", A_move.as_view(), name="a_move"),
]