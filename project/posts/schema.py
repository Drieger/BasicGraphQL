import graphene
from graphql_relay.node.node import from_global_id
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from django.contrib.auth.models import User as UserModel
from posts.models import Post as PostModel


class PostNode(DjangoObjectType):
    """Post node schema definition."""

    class Meta:
        model = PostModel
        interfaces = (graphene.Node, )
        filter_fields = ['author__username', 'title']

    @classmethod
    def get_node(cls, info, id):
        return PostModel.objects.get(pk=id)


class UpdatePostMutation(graphene.Mutation):
    """Post update mutation schema definition."""

    class Arguments:
        id = graphene.String(required=True)
        author_id = graphene.String()
        title = graphene.String()
        text = graphene.String()

    success = graphene.Boolean()
    post = graphene.Field(PostNode)

    def mutate(self, info, **arguments):
        """Update an existing post."""
        post_id = from_global_id(arguments.pop('id'))[1]
        post = PostModel.objects.get(pk=post_id)

        if not post:
            print("=" * 100)
            print("schema.py@41")
            print("Erro while updating post")
            print("=" * 100)
            return UpdatePostMutation(success=False)

        for k, v in arguments.items():
            setattr(post, k, v)
        post.save()
        return UpdatePostMutation(success=True, post=post)


class CreatePostMutation(graphene.Mutation):
    """Post creation mutation schema definition."""

    class Arguments:
        author_id = graphene.String(required=True)
        title = graphene.String(required=True)
        text = graphene.String()

    success = graphene.Boolean()
    post = graphene.Field(PostNode)

    def mutate(self, info, **arguments):
        """Create a new post."""
        title = arguments.get('title')
        text = arguments.get('text')

        # Get author id from `relay` id and find author on database
        author_id = from_global_id(arguments.get('author_id'))[1]
        author = UserModel.objects.get(pk=author_id)

        # Get post id from `relay` id and find it on database
        post_id = from_global_id(arguments.pop('id'))[1]
        post = PostModel.objects.get(pk=post_id)

        if not author:
            print("=" * 100)
            print("schema.py@41")
            print("We should return an error here")
            print("=" * 100)
            return CreatePostMutation(success=False)

        post = PostModel.objects.create(title=title, author=author, text=text)
        return CreatePostMutation(success=True, post=post)




class Query(object):
    """Posts app query definition."""

    post = graphene.Node.Field(PostNode)
    all_posts = DjangoFilterConnectionField(PostNode)
