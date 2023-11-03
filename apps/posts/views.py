from django.core.exceptions import ValidationError
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.posts.models import Post
from apps.posts.services import PostService
from apps.posts.serializers import PostSerializer
from apps.posts.exceptions import PostNotFoundException

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    service_class = PostService()
    serializer_class = PostSerializer
    permissions = [IsAuthenticatedOrReadOnly]
    
    def create(self, request, *args, **kwargs) -> Response:
        try:
            post = self.service_class.create_post(request.user, request.data)
        except ValidationError as e:
            return Response({"error": e.message_dict}, status=status.HTTP_400_BAD_REQUEST)
        return Response(post, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=["POST"], url_path="like", url_name="post-like")
    def post_like(self, request, pk, *args, **kwargs) -> Response:
        self.service_class.like_post(request.user, pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    @post_like.mapping.delete
    def post_unlike(self, request, pk, *args, **kwargs) -> Response:
        self.service_class.unlike_post(request.user, pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
