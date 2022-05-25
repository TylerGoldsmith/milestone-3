# Dependencies
from django.db import models
from django_cryptography.fields import encrypt
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# User Manager


class UserManager(BaseUserManager):

    def Create_User_Account(self, username, email, enc_pw_ua=None, **kwargs):
        if enc_pw_ua is None:
            raise TypeError('Users must have a password.')
        if username is None:
            raise TypeError('Users must have a username.')
        if email is None:
            raise TypeError('Users must have an email.')

        username = self.model(
            username=username, email=self.normalize_email(email))
        username.set_password(enc_pw_ua)
        username.save(using=self._db)

        return self.username, self.enc_pw_ua, self.email, self

    def Create_Admin_Account(self, username, email, enc_pw_ua):

        if enc_pw_ua is None:
            raise TypeError('Admin must have a password.')
        if email is None:
            raise TypeError('Admin must have an email.')
        if username is None:
            raise TypeError('Admin must have an username.')

        username = self.create_user(
            username, email, enc_pw_ua)
        username.is_superuser = True
        username.is_staff = True
        username.save(using=self._db)

        return self.username, self.enc_pw_ua, self.email, self

    def get_by_natural_key(self, email):
        return self.get(email=email)


# User Data Models
# User account Model
class User_Account(AbstractBaseUser):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(db_index=True, max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.CharField(db_index=True, unique=True,  null=True, blank=True, max_length=50)
    enc_pw_ua = models.CharField(max_length=25)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = UserManager()

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True


    class User_Account_Serialization:
        ordering = ['created']

    def __str__(self):
        return f"{self.email}"

# Review
class Review(models.Model):
    id = models.BigAutoField(primary_key=True)
    review = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now_add=True, default='')
    user_account_id = models.ForeignKey(User_Account, on_delete=models.CASCADE)

    class Review_Serialization:
        ordering = ['created']

    def __str__(self):
        return id.self, review.self, created_at.self, user_account_id.self

# Video Game Models
# Genre Model


class Genre(models.Model):
    id = models.BigAutoField(primary_key=True)
    genre_name = models.CharField(max_length=30)

    class Genre_Serialization:
        ordering = ['created']

    def __str__(self):
        return id.self, genre_name.self

# Game Model


class Game(models.Model):
    id = models.BigAutoField(primary_key=True)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    review_id = models.ForeignKey(Review, default="", on_delete=models.CASCADE)
    game_name = models.CharField(max_length=30)
    game_description = models.TextField()

    class Game_Serialization:
        ordering = ['created']

    def __str__(self):
        return id.self, genre_id.self, review_id.self, game_name.self, game_description.self

# Publisher Model


class Publisher(models.Model):
    id = models.BigAutoField(primary_key=True)
    publisher_name = models.CharField(max_length=30)

    class Publisher_Serialization:
        ordering = ['created']

    def __str__(self):
        return id.self, publisher_name.self

# Game Publisher Model


class Game_Publisher(models.Model):
    id = models.BigAutoField(primary_key=True)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    game_publisher_id = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    class Game_Publisher_Serialization:
        ordering = ['created']

    def __str__(self):
        return id.self, game_id, game_publisher_id

# Platform Model


class Platform(models.Model):
    id = models.BigAutoField(primary_key=True)
    platform_name = models.CharField(max_length=30)

    class Publisher_Serialization:
        ordering = ['created']

    def __str__(self):
        return id.self, platform_name.self

# Game Platform Model


class Game_Platform(models.Model):
    id = models.BigAutoField(primary_key=True)
    platform_id = models.ForeignKey(Platform, on_delete=models.CASCADE)
    release_year = models.CharField(max_length=4)

    class Game_Platform_Serialization:
        ordering = ['created']

    def __str__(self):
        return id.self, platform_id.self, release_year.self
