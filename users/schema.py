# -*- coding: utf-8 -*-
"""users.schema"""
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth import login
import graphene
from graphene_django.types import DjangoObjectType
from graphql_jwt.shortcuts import get_token

class UserType(DjangoObjectType):

    """UserType"""

    class Meta:
        """Meta"""
        model = get_user_model()
        exclude = ('password',)


class Login(graphene.Mutation):

    """Login"""
    user = graphene.String()
    token = graphene.String()

    class Arguments:
        """Arguments"""
        username = graphene.String()

    @classmethod
    def mutate(cls, root, info, username):
        """Mutate"""
        user = authenticate(username=username, password=username)

        if user is None:
            new_user = get_user_model()(username = username)
            new_user.set_password(username)
            new_user.save()
            user = authenticate(username=username, password=username)

        if not user.is_active:
            raise Exception('It seems your account has been disabled')

        login(info.context, user)
        return Login(token=get_token(user), user=user.username)



class Mutation(graphene.ObjectType):

    """Mutation"""

    authenticate = Login.Field()
