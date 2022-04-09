"""Project schema"""

import graphene

from songs.schema import Query as SongsAppQuery
from songs.schema import Mutation as SongsAppMutation


class Query(SongsAppQuery, graphene.ObjectType):
    ping = graphene.String()

    def resolve_ping(self, info):
        return "Pong!"


class Mutation(SongsAppMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
