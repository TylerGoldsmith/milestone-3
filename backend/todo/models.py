# Dependencies
from django.db import models
from django_cryptography.fields import encrypt

# User Data Models
# User account Model
class User_Account(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_account_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    enc_em_ua = encrypt(models.CharField(max_length=30))
    enc_pw_ua = encrypt(models.CharField(max_length=25))

    class User_Account_Serialization:
        ordering = ['created']

# Review
class Review(models.Model):
    id = models.BigAutoField(primary_key=True)
    review = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now_add=True, default='')
    user_account_id = models.ForeignKey(User_Account, on_delete=models.CASCADE)

    class Review_Serialization:
        ordering = ['created']

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
    review_id = models.ForeignKey(Review, default="", on_delete=models.CASCADE)
    game_name = models.CharField(max_length=30)
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
    release_year = models.CharField(max_length=4)

    class Game_Platform_Serialization:
        ordering = ['created']
