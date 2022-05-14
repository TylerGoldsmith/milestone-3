# Dependencies
from django.db import models


# Game Platform Model
class game_platform(models.Model):
    id = models.BigAutoField(primary_key=True)
    game_publisher_id = models.BigAutoField(primary_key=True)
    platform_id = models.ForeignKey(Platform, on_delete=models.CASCADE)
    release_year = models.SmallIntegerField(max_length=4, min_length=4)

    def _str_(self):
        return self.title

# Platform Model
class platform(models.Model):
    id = models.BigAutoField(primary_key=True)
    platform_name = models.CharField(max_length=30)


    def _str_(self):
        return self.title

# Game Publisher Model
class game_publisher(models.Model):
    id = models.BigAutoField(primary_key=True)
    game_id = models.ForeignKey(Platform, on_delete=models.CASCADE)
    publisher_id = models.BigAutoField()

    def _str_(self):
        return self.title


# Publisher Model
class publisher(models.Model):
    id = models.BigAutoField(primary_key=True)
    publisher_name = models.CharField(max_length=30)

    def _str_(self):
        return self.title

# Game Model
class game(models.Model):
    id = models.BigAutoField(primary_key=True)
    genre_id = models.ForeignKey(Platform, on_delete=models.CASCADE)
    platform_name = models.CharField(max_length=30)
    game_description = models.TextField()

    def _str_(self):
        return self.title

# Genre Model
class genre(models.Model):
    id = models.BigAutoField(primary_key=True)
    genre_name = models.CharField(max_length=30)

    def _str_(self):
        return self.title
