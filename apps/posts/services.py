from django.db import transaction
from django.db.models import Q

from apps.posts.models import Post, Like
from apps.users.models import User
from apps.posts.serializers import PostDict, PostCreateSerializer, PostSerializer
from apps.posts.exceptions import PostNotFoundException

from typing import Any


class PostService:
    
    @transaction.atomic
    def create_post(self, user: User, data: dict[str, Any]) -> PostDict:
        
        serializer = PostCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        
        data = serializer.validated_data
        data["author"] = user
        
        post = Post(**data)
        post.full_clean()
        post.save()
        
        response = PostSerializer(post).data
        
        return response
    
    @transaction.atomic
    def like_post(self, user: User, post_id: int) -> None:
        
        if not (post := Post.objects.filter(id=post_id).first()):
            raise PostNotFoundException()
        
        if like := Like.objects.filter(Q(user=user) & Q(post=post)):
            return
        
        like = Like(
            user=user,
            post=post
        )
        like.full_clean()
        like.save()
    
    @transaction.atomic
    def unlike_post(self, user: User, post_id: int) -> None:
        
        if not (post := Post.objects.filter(id=post_id).first()):
            raise PostNotFoundException()
        
        if not (like := Like.objects.filter(Q(user=user) & Q(post=post))):
            return
        
        like.delete()
