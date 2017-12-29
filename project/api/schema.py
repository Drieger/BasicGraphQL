import graphene
import users.schema as users_schema
import posts.schema as posts_schema


class Query(users_schema.Query, posts_schema.Query, graphene.ObjectType):
    """Query object definition."""

    pass


schema = graphene.Schema(query=Query)
