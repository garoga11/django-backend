'''Posts model srializer'''

#Django REST framework

from rest_framework import serializers

#models
from posts.models import Author, Post, Author
from django.contrib.auth.models import User

class PostModelSerializer(serializers.ModelSerializer):
    '''Post model serializer'''

    class Meta:
        model = Post
        fields = ['pk', 'image', 'title', 'likes', 'created_at']

class GetAuthorSerializer(serializers.ModelSerializer):
    """Get author username from user model"""

    class Meta:
        model =User
        fields =['username']

class AuthorModelSerializer(serializers.ModelSerializer):
    """Author model serializer"""

    author = GetAuthorSerializer(read_only=True)

    class Meta:
        model = Author
        fields = ['author', 'post']
        depth=1