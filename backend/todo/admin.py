# Dependencies
from django.contrib import admin
from .models import User_Account, Review, Genre, Game, Publisher, Game_Publisher, Platform, Game_Platform

# User Account
class User_Account_Admin(admin.ModelAdmin):
    list_display = ('id', 'user_account_name', 'created_at', 'enc_em_ua', 'enc_pw_ua')

admin.site.register(User_Account, User_Account_Admin)

# Review
class Review_Admin(admin.ModelAdmin):
    list_display = ('id', 'review', 'created_at', 'user_account_id')

admin.site.register(Review, Review_Admin)

# Genre
class Genre_Admin(admin.ModelAdmin):
    list_display = ('id', 'genre_name')

admin.site.register(Genre, Genre_Admin)

# Game
class Game_Admin(admin.ModelAdmin):
    list_display = ('id', 'genre_id', 'game_name','game_description')

admin.site.register(Game, Game_Admin)
# Publisher
class Publisher_Admin(admin.ModelAdmin):
    list_display = ('id', 'publisher_name')

admin.site.register(Publisher, Publisher_Admin)

# Game Publisher
class Game_Publisher_Admin(admin.ModelAdmin):
    list_display = ('id', 'game_id', 'game_publisher_id')

admin.site.register(Game_Publisher, Game_Publisher_Admin)

# Platform
class Platform_Admin(admin.ModelAdmin):
    list_display = ('id', 'platform_name')

admin.site.register(Platform, Platform_Admin)

# Game Platform
class Game_Platform_Admin(admin.ModelAdmin):
    list_display = ('id', 'platform_id', 'release_year')

admin.site.register(Game_Platform, Game_Platform_Admin)