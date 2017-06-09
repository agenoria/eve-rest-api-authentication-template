# set the possible resource methods for all branches
RESOURCE_METHODS = ['GET', 'POST']

DOMAIN = {
    # create a `user` branch
    'user': {
        'schema': {
            'username': {
                'type': 'string',
                'unique': True
            },
            'password': {
                'type': 'string'
            },
        },
        'additional_lookup': {
            'url': 'regex("[\w]+")',
            'field': 'username',
        }
    },
    # create a `people` branch
    'people': {
        'schema': {
            'name': {
                'type': 'string',
                'unique': True
            }
        },
        # this line is CRITICAL as it allows both GET and POST requests to this branch (without any authentication)
        'public_methods': ["GET", "POST"],
        'additional_lookup': {
            'url': 'regex("[\w]+")',
            'field': 'name',
        }
    }
}
