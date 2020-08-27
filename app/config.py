import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    
    SQLALCHEMY_DATABASE_URI = os.getenv(
                                'SQLALCHEMY_URI',
                                'postgresql://{user}:{passwd}@{host}/{dbname}'.format(
                                user   = os.getenv('POSTGRES_USER', "postgres"),
                                passwd = os.getenv('POSTGRES_PASSWORD', "saugat123"),
                                host   = os.getenv('POSTGRES_HOST', "localhost"),
                                dbname = os.getenv('POSTGRES_DB', "flask_app"),
        )
        )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

