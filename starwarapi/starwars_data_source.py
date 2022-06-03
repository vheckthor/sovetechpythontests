'''star wars data source'''
import requests

BASE_URL = 'https://swapi.dev/api/'

def get_people(page):
    '''Get people from starwars API'''
    url = BASE_URL + 'people/?page=' + str(page)
    response = requests.get(url)
    return response.json()

def get_person(name):
    '''Get person from starwars API'''
    url = BASE_URL + 'people/?search=' + name
    response = requests.get(url)
    return response.json()

def get_homeworld(url):
    '''Get homeworld from starwars API'''
    response = requests.get(url)
    return response.json()
