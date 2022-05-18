"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Dependencies
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include(router.urls)),
# user account
    path('user_accounts/', views.user_account_list),
    path('user_account/<int:pk>/', views.user_account_detail),
# review
    path('reviews/', views.review_list),
    path('review/<int:pk>/', views.review_detail),
# genre
    path('genres/', views.genre_list),
    path('genre/<int:pk>/', views.genre_detail),
# games
    path('games/', views.game_list),
    path('game/<int:pk>/', views.game_detail),
# publisher
    path('publishers/', views.publisher_list),
    path('publisher/<int:pk>/', views.publisher_detail),
# game publisher
    path('game_publishers/', views.game_publisher_list),
    path('game_publisher/<int:pk>/', views.game_publisher_detail),
# platform
    path('platforms/', views.platform_list),
    path('platform/<int:pk>/', views.platform_detail),
# game platform
    path('game_platforms/', views.game_platform_list),
    path('game_platform/<int:pk>/', views.game_platform_detail),
]