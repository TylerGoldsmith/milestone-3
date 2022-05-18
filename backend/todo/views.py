# Dependencies
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from rest_framework import viewsets
# Video Game Imports
from .serializers import Model_Serializer
from .models import Review, Genre, Game, Publisher, Game_Publisher, Platform, Game_Platform
# 
# User Views
# 
# User Account View
# 
@csrf_exempt
def user_account_list(request):
# GET all
    if request.method == 'GET':
        user_accounts = User_Account.objects.all()
        serializer = Model_Serializer(user_accounts, many=True)
        return JsonResponse(serializer.data, safe=False)
# POST
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Model_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
# 
# Get Put or Delete
@csrf_exempt
def user_account_detail(request, pk):
    try:
        user_account = User_Account.objects.get(pk=pk)
    except User_Account.DoesNotExist:
        return HttpResponse(status=404)
# GET
    if request.method == 'GET':
        serializer = Model_Serializer(review)
        return JsonResponse(serializer.data)
# PUT
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Model_Serializer(user_account, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
# DELETE
    elif request.method == 'DELETE':
        user_account.delete()
        return HttpResponse(status=204)
# 
# Review View
# 
@csrf_exempt
def review_list(request):
# GET all
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = Model_Serializer(reviews, many=True)
        return JsonResponse(serializer.data, safe=False)
# POST
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Model_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
# 
# Get Put or Delete
@csrf_exempt
def review_detail(request, pk):
    try:
        review = Review.objects.get(pk=pk)
    except Review.DoesNotExist:
        return HttpResponse(status=404)
# GET
    if request.method == 'GET':
        serializer = Model_Serializer(review)
        return JsonResponse(serializer.data)
# PUT
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Model_Serializer(review, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
# DELETE
    elif request.method == 'DELETE':
        review.delete()
        return HttpResponse(status=204)
# 
# Video Game Views
# 
# Genre
# 
# Full list or Post
@csrf_exempt
def genre_list(request):
# GET all
    if request.method == 'GET':
        genres = Genre.objects.all()
        serializer = Model_Serializer(genres, many=True)
        return JsonResponse(serializer.data, safe=False)
# POST
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Model_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
# 
# Get Put or Delete
@csrf_exempt
def genre_detail(request, pk):
    try:
        genre = Genre.objects.get(pk=pk)
    except Genre.DoesNotExist:
        return HttpResponse(status=404)
# GET
    if request.method == 'GET':
        serializer = Model_Serializer(genre)
        return JsonResponse(serializer.data)
# PUT
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Model_Serializer(genre, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
# DELETE
    elif request.method == 'DELETE':
        genre.delete()
        return HttpResponse(status=204)
# 
# Game
# 
# Full list or Post
@csrf_exempt
def game_list(request):
# GET all
    if request.method == 'GET':
        games = Game.objects.all()
        serializer = Model_Serializer(games, many=True)
        return JsonResponse(serializer.data, safe=False)
# POST
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Model_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
# 
# Get Put or Delete
@csrf_exempt
def game_detail(request, pk):
    try:
        game = Game.objects.get(pk=pk)
    except Game.DoesNotExist:
        return HttpResponse(status=404)
# GET
    if request.method == 'GET':
        serializer = Model_Serializer(game)
        return JsonResponse(serializer.data)
# PUT
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Model_Serializer(game, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
# DELETE
    elif request.method == 'DELETE':
        game.delete()
        return HttpResponse(status=204)
# 
# Publisher
# 
# Full list or post
@csrf_exempt
def publisher_list(request):
# GET all
    if request.method == 'GET':
        publishers = Publisher.objects.all()
        serializer = Model_Serializer(publishers, many=True)
        return JsonResponse(serializer.data, safe=False)
# POST
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Model_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
# 
# Get Put or Delete
@csrf_exempt
def publisher_detail(request, pk):
    try:
        publisher = Publisher.objects.get(pk=pk)
    except Publisher.DoesNotExist:
        return HttpResponse(status=404)
# GET
    if request.method == 'GET':
        serializer = Model_Serializer(publisher)
        return JsonResponse(serializer.data)
# PUT
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Model_Serializer(publisher, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
# DELETE
    elif request.method == 'DELETE':
        publisher.delete()
        return HttpResponse(status=204)
# 
# Game Publisher
# 
# Full list or Post
@csrf_exempt
def game_publisher_list(request):
# GET all
    if request.method == 'GET':
        game_publishers = Game_Publisher.objects.all()
        serializer = Model_Serializer(game_publishers, many=True)
        return JsonResponse(serializer.data, safe=False)
# POST
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Model_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
# 
# Get Put or Delete
@csrf_exempt
def game_publisher_detail(request, pk):
    try:
        game_publisher = Game_Publisher.objects.get(pk=pk)
    except Game_Publisher.DoesNotExist:
        return HttpResponse(status=404)
# GET
    if request.method == 'GET':
        serializer = Model_Serializer(game_publisher)
        return JsonResponse(serializer.data)
# PUT
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Model_Serializer(game_publisher, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
# DELETE
    elif request.method == 'DELETE':
        game_publisher.delete()
        return HttpResponse(status=204)
# 
# Platform
# 
# Full list or Post
@csrf_exempt
def platform_list(request):
# GET all
    if request.method == 'GET':
        platforms = Platform.objects.all()
        serializer = Model_Serializer(platforms, many=True)
        return JsonResponse(serializer.data, safe=False)
# POST
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Model_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
# 
# Get Put or Delete
@csrf_exempt
def platform_detail(request, pk):
    try:
        platform = Platform.objects.get(pk=pk)
    except Platform.DoesNotExist:
        return HttpResponse(status=404)
# GET
    if request.method == 'GET':
        serializer = Model_Serializer(platform)
        return JsonResponse(serializer.data)
# PUT
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Model_Serializer(platform, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
# DELETE
    elif request.method == 'DELETE':
        platform.delete()
        return HttpResponse(status=204)
# 
# Game Platform
# 
# Full list or Post
@csrf_exempt
def game_platform_list(request):
# GET all
    if request.method == 'GET':
        game_platforms = Game_Platform.objects.all()
        serializer = Model_Serializer(game_platforms, many=True)
        return JsonResponse(serializer.data, safe=False)
# POST
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Model_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
# 
# Get Put or Delete
@csrf_exempt
def game_platform_detail(request, pk):
    try:
        game_platform = Game_Platform.objects.get(pk=pk)
    except Game_Platform.DoesNotExist:
        return HttpResponse(status=404)
# GET
    if request.method == 'GET':
        serializer = Model_Serializer(game_platform)
        return JsonResponse(serializer.data)
# PUT
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Model_Serializerso(game_platform, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
# DELETE
    elif request.method == 'DELETE':
        game_platform.delete()
        return HttpResponse(status=204)