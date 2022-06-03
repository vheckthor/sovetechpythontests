'''Module for schema'''
from graphene import ObjectType, String, Int, Field, List
from graphql_jwt.decorators import login_required
from starwarapi.starwars_data_source import get_people, get_person

class CustomObject:
    '''Custom object to deserialize json to python object'''
    def __init__(self, dico=None):
        if dico is not None:
            for key, value in dico.items():
                setattr(self, key, value)

def json_to_obj(data):
    '''Convert JSON data to native Python objects'''
    response = CustomObject(data)
    return response

class Person(ObjectType):
    '''A person in the Star Wars universe'''
    name = String()
    height = String()
    mass = String()
    gender = String()
    homeworld = String()

class People(ObjectType):
    '''The list of people in star wars'''
    count = Int()
    next = String()
    previous = String()
    results = List(Person)


class Query(ObjectType):
    '''Query for starwars'''
    people = Field(People, page = Int(required=True))
    person = Field(People, name = String(required=True))

    @login_required
    def resolve_people(self, info, page):
        '''Resolve people'''
        data = get_people(page)
        return json_to_obj(data)

    @login_required
    def resolve_person(self, info, name):
        '''Resolve person'''
        data = get_person(name)
        return json_to_obj(data)
