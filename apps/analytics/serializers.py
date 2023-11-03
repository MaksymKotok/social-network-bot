from rest_framework import serializers
from apps.posts.models import Like
from apps.users.models import User

from typing import TypedDict
from config.utils import get_typedict_fields


class LikePostAnalyticsDict(TypedDict):
    day: str
    likes: int


class LikePostAnalyticsSerializer(serializers.ModelSerializer):
    
    day = serializers.DateField()
    likes = serializers.IntegerField()
    
    class Meta:
        model = Like
        fields = get_typedict_fields(LikePostAnalyticsDict)
        

class UserActivityDict(TypedDict):
    username: str
    email: str
    last_login: str
    last_request: str
    
    
class UserActivitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = get_typedict_fields(UserActivityDict)
