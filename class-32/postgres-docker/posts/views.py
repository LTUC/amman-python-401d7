from django.shortcuts import render
from rest_framework import generics
from .serializers import PostSerialzer
from .models import Post

# CR views
class PostList(generics.ListCreateAPIView):
    # queryset = Post.objects.filter(published = True)
    queryset = Post.objects.all()
    serializer_class = PostSerialzer

# RUD view
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialzer


# class PostCreate():
#     pass

# class PostUpdate():
#     pass

# class PostDelete():
#     pass