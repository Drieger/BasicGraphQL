from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    """Post definition."""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    title = models.CharField(
        max_length=128,
        null=False
    )

    text = models.TextField()

    def __str__(self):
        """Return a string representation of this objects."""
        return self.title
