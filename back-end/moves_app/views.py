from django.shortcuts import render
from .serializers import MoveSerializer

class All_moves(APIView):
    # establish a get method that will be triggered by GET requests
    def get(self, request):
        # utilize your ModelSerializer to serialize your queryset and return a proper response with DRF's Response
        moves = MoveSerializer(Move.objects.all(), many=True)
        return Response(moves.data)
# Create your views here.
class A_move(APIView):
    def get(self, request, name):
        move = Move.objects.get(name = name.title())
        return Response(MoveSerializer(move).data)
