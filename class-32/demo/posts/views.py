from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import PostSerialzer
from .models import Post
from .permissions import IsAuthenticatedOrReadOnly


class PostList(generics.ListCreateAPIView):
    # queryset = Post.objects.filter(published = True)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerialzer
    

# RUD view
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialzer
    permission_classes = (IsAuthenticatedOrReadOnly,)


# class PostCreate():
#     pass

# class PostUpdate():
#     pass

# class PostDelete():
#     pass