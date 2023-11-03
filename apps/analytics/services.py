from django.db.models import Q

from apps.posts.models import Like, Post
from apps.users.models import User
from apps.analytics.serializers import (
    LikePostAnalyticsSerializer,
    LikePostAnalyticsDict,
    UserActivitySerializer,
    UserActivityDict
)
from apps.analytics.exceptions import IncorrectDateRangeException
from apps.posts.exceptions import PostNotFoundException


class PostAnalyticsService:

    def list_like_analytics(self, date_from: str = None, date_to: str = None) -> list[LikePostAnalyticsDict]:
        if date_from and date_to:
            if date_from > date_to:
                raise IncorrectDateRangeException()
            
            likes = Like.by_day.filter(Q(day__gte=date_from) & Q(day__lte=date_to))
        elif date_from and not date_to:
            likes = Like.by_day.filter(day__gte=date_from)
        elif not date_from and date_to:
            likes = Like.by_day.filter(day__lte=date_to)
        else:
            likes = Like.by_day.all()

        response = LikePostAnalyticsSerializer(likes, many=True).data                
        return response
    
    def retrieve_like_analytics(self, post_id: int, date_from: str = None, date_to: str = None) -> list[LikePostAnalyticsDict]:
        if not (post := Post.objects.filter(id=post_id).first()):
            raise PostNotFoundException()
        
        if date_from and date_to:
            if date_from > date_to:
                raise IncorrectDateRangeException()
            
            likes = Like.by_day.filter(Q(day__gte=date_from) & Q(day__lte=date_to) & Q(post=post))
        elif date_from and not date_to:
            likes = Like.by_day.filter(Q(day__gte=date_from) & Q(post=post))
        elif not date_from and date_to:
            likes = Like.by_day.filter(Q(day__lte=date_to) & Q(post=post))
        else:
            likes = Like.by_day.filter(post=post)

        response = LikePostAnalyticsSerializer(likes, many=True).data                
        return response
    
    
class UserActivityService:
    
    def user_activity(self) -> list[UserActivityDict]:
        users = User.objects.all()
        response = UserActivitySerializer(users, many=True).data
        return response
