from typing import TypedDict

from rest_framework import serializers

from apps.posts.models import Post
from apps.users.models import User
from config.utils import get_typedict_fields


class PostCreateDict(TypedDict):
    name: str
    text: str
    
    
class PostCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = get_typedict_fields(PostCreateDict)
        
        
class PostUserDict(TypedDict):
    username: str
    email: str
    
    
class PostUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = get_typedict_fields(PostUserDict)
    

class PostDict(TypedDict):
    id: int
    author: PostUserDict
    name: str
    text: str
    

class PostSerializer(serializers.ModelSerializer):
    
    author = PostUserSerializer()
    
    class Meta:
        model = Post
        fields = get_typedict_fields(PostDict)
