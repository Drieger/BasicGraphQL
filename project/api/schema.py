import graphene
import users.schema as users_schema
import posts.schema as posts_schema


class Query(users_schema.Query, posts_schema.Query, graphene.ObjectType):
    """Query object definition."""

    pass


class Mutation(graphene.ObjectType):
    """Mutation object definition."""

    create_post = posts_schema.CreatePostMutation.Field()
    update_post = posts_schema.UpdatePostMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
