# Template for a Simple API with Authentication Using Python Eve

This is a simple foundation for building API's using [Eve](http://python-eve.org/) with authentication.

`setup.sh` contains basic instructions for setting up mongo (as the backend for the API) and redis (to allow rate-limiting on the API). This script may not be complete and may not work for you (I primarily intend this as a guideline to memorialize some of the tips and tricks I learned while setting up an API).

A similar template without authentication can be found here: [https://github.com/agenoria/eve-rest-api-template](https://github.com/agenoria/eve-rest-api-template).

## Authentication

This example has two branches: `people` and `user`. By default, both branches accept `GET` and `POST` requests (this is defined by the line that reads: [`RESOURCE_METHODS = ['GET', 'POST']` in settings.py](https://github.com/agenoria/eve-rest-api-authentication-template/blob/master/settings.py#L2)).

In terms of authentication, the request and methods are handled as follows:

| Resource | Method | Authentication? |
|---|---|---|
| people | GET | No† |
| people | POST | No† |
| user | GET | Yes (from database)\* |
| user | POST | Yes (hardcoded)\*\* |

† - Both `GET` and `POST` requests are allowed to the `people` branch by [line 30 settings.py](https://github.com/agenoria/eve-rest-api-authentication-template/blob/master/settings.py#L30).

\* - `GET` requests to the `user` branch are authenticated against the database as defined in [run.py](https://github.com/agenoria/eve-rest-api-authentication-template/blob/master/run.py#L10).

\*\* - `POST` requests to the `user` branch are authenticated against a hardcoded username and password as defined in [run.py](https://github.com/agenoria/eve-rest-api-authentication-template/blob/master/run.py#L10). This should go without saying, but putting hardcoded usernames and passwords in API authentication systems is a **very bad idea**. **Don't do it!**

## Helpful Queries

Once you have the API up and running, here are some helpful queries:

GET:

`curl http://127.0.0.1:5000/people` (no authentication required)

`curl http://127.0.0.1:5000/user` (requires authentication)

POST:

`curl -d '[{"name": "Alvaro"}]' -H 'Content-Type: application/json' http://127.0.0.1:5000/people` (no authentication required b/c POST method is one of the public methods for this branch)

`curl -d '[{"username": "Alvaro", "password": "123456"}]' -u <USERNAME>:<PASSWORD> -H 'Content-Type: application/json' http://127.0.0.1:5000/user` (requires authentication by default b/c anytime we are using a class to manage authentication, all POST requests must have authentication unless declared otherwise)
