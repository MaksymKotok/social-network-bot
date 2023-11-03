from django.core.exceptions import ValidationError
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser


from apps.analytics.exceptions import IncorrectDateRangeException
from apps.posts.exceptions import PostNotFoundException
from apps.analytics.services import PostAnalyticsService, UserActivityService


class PostAnalyticsListAPIView(ListAPIView):
    permission_classes = [IsAdminUser]
    service_class = PostAnalyticsService()
    
    def get(self, request, *args, **kwargs) -> Response:
        try:
            likes = self.service_class.list_like_analytics(date_from=request.GET.get("date_from", None), date_to=request.GET.get("date_to", None))
        except ValidationError as e:
            return Response({"error": e.message}, status=status.HTTP_400_BAD_REQUEST)
        return Response(likes, status=status.HTTP_200_OK)
    
    
class PostAnalyticsRetrieveAPIView(RetrieveAPIView):
    permission_classes = [IsAdminUser]
    service_class = PostAnalyticsService()
    
    def get(self, request, pk, *args, **kwargs) -> Response:
        try:
            likes = self.service_class.retrieve_like_analytics(post_id=pk, date_from=request.GET.get("date_from", None), date_to=request.GET.get("date_to", None))
        except ValidationError as e:
            return Response({"error": e.message}, status=status.HTTP_400_BAD_REQUEST)
        return Response(likes, status=status.HTTP_200_OK)
    
    
class UserActivityAPIView(ListAPIView):
    permission_classes = [IsAdminUser]
    service_class = UserActivityService()
    
    def get(self, request, *args, **kwargs) -> Response:
        activity = self.service_class.user_activity()
        return Response(activity, status=status.HTTP_200_OK)
