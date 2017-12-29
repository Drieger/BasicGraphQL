import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from django.contrib.auth.models import User as UserModel
from users.models import Profile as ProfileModel


class ProfileNode(DjangoObjectType):
    """User profile type schema definition."""

    class Meta:
        model = ProfileModel
        interfaces = (graphene.Node, )

    @classmethod
    def get_node(cls, info, id):
        return ProfileModel.objects.get(pk=id)


class UserNode(DjangoObjectType):
    """User type schema definition."""

    class Meta:
        model = UserModel
        interfaces = (graphene.Node, )
        filter_fields = ['username']

    @classmethod
    def get_node(cls, info, id):
        return UserModel.objects.get(pk=id)


class Query(object):
    """Users app query definition."""

    user = graphene.Node.Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)
