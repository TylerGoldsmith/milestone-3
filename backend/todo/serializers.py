from rest_framework import serializers
from .models import User_Account, Review, Genre, Game, Publisher, Game_Publisher, Platform, Game_Platform

class Model_Serializer(serializers.ModelSerializer):
    # class User_Account_Serialization(Model_Serializer):
    #     model: User_Account
    #     fields: ('id', 'user_account_name', 'enc_em_ua', 'enc_pw_ua')

    class Review_Serialization:
        model: Review
        fields: ('id', 'review', 'user_account_id')

    class Genre_Serialization:
        model = Genre
        fields = ('id', 'genre_name')

    class Game_Serialization:
        model = Game
        fields = ('id', 'genre_id', 'platform_name','game_description')
        # change platform name to game name

    class Publisher_Serialization:
        model = Publisher
        fields = ('id', 'publisher_name')

    class Game_Publisher_Serialization:
        model = Game_Publisher
        fields = ('id', 'game_id', 'game_publisher_id')

    class Platform_Serialization:
        model = Platform
        fields = ('id', 'platform_name')

    class Game_Platform_Serialization:
        model = Game_Platform
        fields = ('id', 'platform_id', 'release_year')
