## Python Software Engineer Test SovTech
## Requirements
  1. You should develop a GraphQL API
  2. Your GraphQL API should wrap the Star Wars API (https://swapi.dev/). 
  3. It should have an authenticate Mutation that, when given an arbitrary username
  returns a JWT ( token ) with the username in the payload
  4. Your GraphQL API should have a Query type that resolves all People
  (https://swapi.dev/api/people/), but only the Person's details (name, height, mass,
  gender, homeworld).
  5. The People Query should cater for pagination, you will notice the next property in
  the response. When given a page number, the respective People page should be
  returned (i.e. https://swapi.dev/api/people/?page=2)
  6. Your GraphQL API should have a Query type that resolves (searches for) a
  particular Person (People) given their name (i.e. https://swapi.dev/api/people/?
  search=Anakin Skywalker)
  7. All your Queries should check and validate a valid JWT issued from the
  authenticate Mutation ( token ) passed along, in the headers with each request.


# Get repo and runserver for Linux.

.. code::

    $ python3.9.5 -m venv /tmp/env && source /tmp/en/bin/activate
    $ git clone https://github.com/vheckthor/sovetechpythontests.git
    $ cd sovtechpytest
    $ pip install setuptools --upgrade && pip install pip --upgrade
    $ pip install -r requirements.txt
    $ cp .env.sample .env  # Please check env variables.
    $ python manage.py migrate
    $ python manage.py runserver 127.0.0.1:8000


# Get repo and runserver for Linux.

.. code::

    $ git clone https://github.com/vheckthor/sovetechpythontests.git
    $ cd sovtechpytest
    $ python -m venv env 
    $ venv env
    $ ./env/Scripts/activate
    $ pip install -r requirements.txt
    $ cp .env.sample .env  # Please check env variables.
    $ python manage.py migrate
    $ python manage.py runserver 127.0.0.1:8000

* Access with your browser.

.. code::

    http://localhost:8000/graphql/


# Test with Insomania.
  -testing with insomania add the JWT token to the header of the request for the Queries.