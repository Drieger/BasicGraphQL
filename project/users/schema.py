import graphene
from graphene_django.types import DjangoObjectType
from django.contrib.auth.models import User as UserModel

from users.models import Profile as ProfileModel


class ProfileType(DjangoObjectType):
    """User profile type schema definition."""

    class Meta:
        model = ProfileModel


class UserType(DjangoObjectType):
    """User type schema definition."""

    class Meta:
        model = UserModel


class Query(graphene.AbstractType):
    """Users app query definition."""

    users = graphene.List(UserType)

    def resolve_users(self, info):
        """Resolve `users` attribute."""
        return UserModel.objects.all()
