import graphene
from graphene_django.types import DjangoObjectType

from posts.models import Post as PostModel


class PostType(DjangoObjectType):
    """Post type schema definition."""

    class Meta:
        model = PostModel


class Query(graphene.ObjectType):
    """Posts app query definition."""

    posts = graphene.List(PostType, author=graphene.String())

    def resolve_posts(self, info, **kwargs):
        """Resolve `posts` attribute."""
        queryset = PostModel.objects
        author = kwargs.get('author')

        if author is not None:
            queryset = queryset.filter(author__username=author)
        return queryset.all()


