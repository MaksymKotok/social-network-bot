from django.urls import path
from rest_framework import routers

from apps.analytics.views import PostAnalyticsListAPIView, PostAnalyticsRetrieveAPIView, UserActivityAPIView

router = routers.DefaultRouter()

urlpatterns = [
    path("analytics/post/", PostAnalyticsListAPIView.as_view(), name="analytics-post-list"),
    path("analytics/post/<int:pk>/", PostAnalyticsRetrieveAPIView.as_view(), name="analytics-post-retrieve"),
    path("analytics/user/activity/", UserActivityAPIView.as_view(), name="user-activity")
]
