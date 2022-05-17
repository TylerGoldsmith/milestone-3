# Dependencies
from django.db import models
from django_cryptography.fields import encrypt

# Video Game Models
# Genre Model
class Genre(models.Model):
    id = models.BigAutoField(primary_key=True)
    genre_name = models.CharField(max_length=30)

    class Genre_Serialization:
        ordering = ['created']

# Game Model
class Game(models.Model):
    id = models.BigAutoField(primary_key=True)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    platform_name = models.CharField(max_length=30)
    game_description = models.TextField()

    class Game_Serialization:
        ordering = ['created']

# Publisher Model
class Publisher(models.Model):
    id = models.BigAutoField(primary_key=True)
    publisher_name = models.CharField(max_length=30)

    class Publisher_Serialization:
        ordering = ['created']

# Game Publisher Model
class Game_Publisher(models.Model):
    id = models.BigAutoField(primary_key=True)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    game_publisher_id = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    class Game_Publisher_Serialization:
        ordering = ['created']

# Platform Model
class Platform(models.Model):
    id = models.BigAutoField(primary_key=True)
    platform_name = models.CharField(max_length=30)


    class Publisher_Serialization:
        ordering = ['created']

# Game Platform Model
class Game_Platform(models.Model):
    id = models.BigAutoField(primary_key=True)
    platform_id = models.ForeignKey(Platform, on_delete=models.CASCADE)
    release_year = models.SmallIntegerField(max_length=4)

    class Game_Platform_Serialization:
        ordering = ['created']
# User Data Models
# Username Model


