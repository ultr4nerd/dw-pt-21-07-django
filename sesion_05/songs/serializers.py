"""Songs app serializers"""

from rest_framework import serializers

from .models import Artist, Album, Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

    def validate_name(self, name):
        if name in ['Bad Bunny', 'Rosalía']:
            raise serializers.ValidationError("No quiero guardar esto >:(")
        return name


class _ArtistSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def validate_name(self, name):
        if name in ['Bad Bunny', 'Rosalía']:
            raise serializers.ValidationError("No quiero guardar esto >:(")
        return name

    def create(self, validated_data):
        return Artist.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
