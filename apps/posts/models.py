from django.db import models
from django.db.models.query import QuerySet

from apps.users.models import User


class Post(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="posts",
        blank=False,
        null=True,
    )
    name = models.CharField(max_length=255)
    text = models.TextField()
    
    def __str__(self) -> str:
        if self.author:
            return f"{self.name} by {self.author}"
        return f"{self.name} by Deleted User"
    
    
class LikeByDayManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().values(day=models.F("time_liked__date")).annotate(likes=models.Count("time_liked")).values("day", "likes").order_by("-day")
    

class Like(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="likes",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="likes",
        blank=False,
        null=True,
    )
    time_liked = models.DateTimeField(auto_now_add=True)
    
    objects = models.Manager()
    by_day = LikeByDayManager()
    
    def __str__(self) -> str:
        if self.user:
            return f"{self.post.name} liked by {self.user.email}"
        return f"{self.post.name} liked by Deleted User"
    
    class Meta:
        unique_together = ("post", "user")
