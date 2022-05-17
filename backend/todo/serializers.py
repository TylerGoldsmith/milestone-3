from rest_framework import serializers
from .models import Genre, Game, Publisher, Game_Publisher, Platform, Game_Platform


class Model_Serializer(serializers.ModelSerializer):
    class Genre_Serialization:
        model = Genre
        fields = ('id', 'genre_name')

    class Game_Serialization:
        model = Game
        fields = ('id', 'genre_id', 'platform_name','game_description')

    class Publisher_Serialization:
        model = Publisher
        fields = ('id', 'publisher_id')

    class Game_Publisher_Serialization:
        model = Game_Publisher
        fields = ('id', 'game_id', 'game_publisher_id')

    class Platform_Serialization:
        model = Platform
        fields = ('id', 'platform_name')

    class Game_Platform_Serialization:
        model = Gane_Platform
        fields = ('id', 'platform_id', 'release_year')