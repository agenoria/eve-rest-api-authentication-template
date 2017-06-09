from eve import Eve
from eve.auth import BasicAuth


class Authenticate(BasicAuth):
    """Define class to handle authentication to API branches not explicitly defined as public (in settings.py)."""

    def check_auth(self, username, password, allowed_roles, resource,
                   method):
        if resource == 'user' and method == 'GET':
            # when making a GET request to the user branch, check the username
            # and password against the database
            user = app.data.driver.db['user']
            user = user.find_one({'username': username, 'password': password})
            if user:
                return True
            else:
                return False
        elif resource == 'user' and method == 'POST':
            # only accept POST requests where username and password are 'admin'
            return username == 'admin' and password == 'admin'
        else:
            return True


if __name__ == '__main__':
    app = Eve(auth=Authenticate)
    app.run()
