'''Tests'''
import json
from graphene_django.utils.testing import GraphQLTestCase
from config.schema import schema

class TestEndPointsCase(GraphQLTestCase):
    '''Test class'''
    GRAPHQL_SCHEMA = schema
    token = None

    def test_query_person_when_no_auth_is_provided(self):
        '''unit test for query with variables'''
        response = self.query(
            '''
            query person($name: String!) {
                person(name: $name) {
                    count
                    next
                    results{
                        name
                        mass
                        height
                    }
                }
            }
            ''',
            op_name='person',
            variables={'name': "Luke Skywalker"},
            headers = {'HTTP_AUTHORIZATION': ""}
        )
        # This validates the status code and if you get errors
        self.assertResponseHasErrors(response)

    def test_query_people_when_no_auth_is_provided(self):
        '''unit test for query with variables'''
        response = self.query(
            '''
            query people($page: Int!) {
                people(page: $page) {
                    count
                    next
                    results{
                        name
                        mass
                        height
                    }
                }
            }
            ''',
            op_name='people',
            variables={'page': 1},
            headers = {'HTTP_AUTHORIZATION': ""}
        )
        self.assertResponseHasErrors(response)

    def test_user_mutation(self):
        '''test user mutation'''
        response = self.query(
            '''
            mutation authenticate($username: String!) {
                authenticate(username: $username) {
                    user
                    token
                }
            }
            ''',
            op_name='authenticate',
            variables={'username': "lakuku"}
        )

        self.token = json.loads(response.content)['data']['authenticate']['token']
        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)

    def test_query_person_when_auth_is_provided(self):
        '''unit test for query with variables'''
        response = self.query(
            '''
            query person($name: String!) {
                person(name: $name) {
                    count
                    next
                    results{
                        name
                        mass
                        height
                    }
                }
            }
            ''',
            op_name='person',
            variables={'name': "Luke Skywalker"},
            headers = {'HTTP_AUTHORIZATION': self.token}
        )
        # This validates the status code and if you get errors
        self.assertEqual(response.status_code, 200)

    def test_query_people_when_auth_is_provided(self):
        '''unit test for query with variables'''
        response = self.query(
            '''
            query people($page: Int!) {
                people(page: $page) {
                    count
                    next
                    results{
                        name
                        mass
                        height
                    }
                }
            }
            ''',
            op_name='people',
            variables={'page': 1},
            headers = {'HTTP_AUTHORIZATION': self.token}
        )
        # This validates the status code and if you get errors
        self.assertEqual(response.status_code, 200)
