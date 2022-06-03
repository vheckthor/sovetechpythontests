# -*- coding: utf-8 -*-
"""config.schema"""

import graphene
import graphql_jwt
import starwarapi.schema
import users.schema


class Query(starwarapi.schema.Query, graphene.ObjectType):

    '''Query'''
    pass


class Mutation(users.schema.Mutation, graphene.ObjectType):

    """Mutation"""

    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
