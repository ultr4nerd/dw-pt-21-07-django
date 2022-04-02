"""Songs app views"""

from django.shortcuts import get_object_or_404

from rest_framework import status, generics, viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Artist, Album, Song
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer

# Generic viewsets


class SongViewset(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticated]


class AlbumViewset(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class ArtistViewset(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


# Bare viewsets

class BareArtistViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = Artist.objects.all()
        serializer = ArtistSerializer(instance=queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        artist = get_object_or_404(Artist, pk=pk)
        serializer = ArtistSerializer(instance=artist)
        return Response(serializer.data)

    def update(self, request, pk=None):
        artist = get_object_or_404(Artist, pk=pk)
        serializer = ArtistSerializer(instance=artist, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk=None):
        artist = get_object_or_404(Artist, pk=pk)
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Generic views


class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


# Bare functions

@api_view(['GET', 'POST'])
def artist_list_view(request):
    if request.method == 'GET':
        queryset = Artist.objects.all()
        serializer = ArtistSerializer(instance=queryset, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def artist_detail_view(request, pk):
    artist = get_object_or_404(Artist, pk=pk)

    if request.method == 'GET':
        serializer = ArtistSerializer(instance=artist)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = ArtistSerializer(instance=artist, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    if request.method == 'DELETE':
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
