from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("auth/", include("djoser.urls")),
    path("auth/", include("apps.authentication.urls")),
    path("admin/", admin.site.urls),
    path("", include("apps.analytics.urls")),
    path("", include("apps.posts.urls")),
    path("", include("apps.users.urls")),
]
