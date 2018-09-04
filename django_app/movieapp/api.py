from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from movieapp.models import MovieInfo
from movieapp.serializers import MovieSerializer


class MovieListView(APIView):
    def get(self):
        movies = MovieInfo.objects.filter()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


class MovieCreateView(APIView):

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)