"""Songs app schema"""

import graphene
from graphene_django import DjangoObjectType

from songs.models import Artist, Album, Song


class ArtistType(DjangoObjectType):
    class Meta:
        model = Artist
        fields = '__all__'


class AlbumType(DjangoObjectType):
    class Meta:
        model = Album
        fields = '__all__'


class SongType(DjangoObjectType):
    class Meta:
        model = Song
        fields = '__all__'


class Query:
    artists = graphene.List(ArtistType, required=True)
    artist = graphene.Field(ArtistType, id=graphene.Int(required=True))
    albums = graphene.List(AlbumType, required=True)
    album = graphene.Field(AlbumType, id=graphene.Int(required=True))
    songs = graphene.List(SongType, required=True)
    song = graphene.Field(SongType, id=graphene.Int(required=True))

    def resolve_artists(self, info):
        return Artist.objects.all()

    def resolve_artist(self, info, id):
        return Artist.objects.get(id=id)

    def resolve_albums(self, info):
        return Album.objects.select_related('artist').all()

    def resolve_album(self, info, id):
        return Album.objects.get(id=id)

    def resolve_songs(self, info):
        return Song.objects.select_related('artist', 'album', 'album__artist').all()

    def resolve_song(self, info, id):
        return Song.objects.get(id=id)


class CreateArtistMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    id = graphene.ID(required=True)
    name = graphene.String(required=True)
    created_at = graphene.String(required=True)
    updated_at = graphene.String(required=True)

    @classmethod
    def mutate(cls, root, info, name):
        artist = Artist.objects.create(name=name)
        return CreateArtistMutation(
            id=artist.id,
            name=artist.name,
            created_at=artist.created_at,
            updated_at=artist.updated_at,
        )


class UpdateArtistMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()

    id = graphene.ID(required=True)
    name = graphene.String(required=True)
    created_at = graphene.String(required=True)
    updated_at = graphene.String(required=True)

    @classmethod
    def mutate(cls, root, info, id, name):
        artist = Artist.objects.get(id=id)
        if name:
            artist.name = name
        artist.save()
        return UpdateArtistMutation(
            id=artist.id,
            name=artist.name,
            created_at=artist.created_at,
            updated_at=artist.updated_at,
        )


class Mutation:
    create_artist = CreateArtistMutation.Field()
    update_artist = UpdateArtistMutation.Field()
