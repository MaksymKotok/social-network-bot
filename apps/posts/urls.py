from django.urls import include, path
from rest_framework import routers

from apps.posts.views import PostViewSet

router = routers.DefaultRouter()
router.register("post", PostViewSet, basename="post")

urlpatterns = [
    path("", include(router.urls)),
]
