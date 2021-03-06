import os

# Cache Config
CACHE_INTERVAL = 10

# Flask Config
class Config(object):
    DEBUG = False
    TESTING = False
    MONGODB_SETTINGS = {
        'host': 'mongodb://localhost:27017/clubhouse'
    }
    SECRET_KEY = "DEV"
    # Integer user_id of your Clubhouse account , you can get it from token json file generated by OpenClubhouse-worker
    OWNER_USER_ID = None


class ProductionConfig(Config):
    MONGODB_SETTINGS = {
        'db': os.getenv("MONGO_DB", "clubhouse"),
        'host': os.getenv("MONGO_HOST", "localhost"),
        'port': int(os.getenv("MONGO_PORT", 27017)),
        'username': os.getenv("MONGO_USERNAME", ""),
        'password': os.getenv("MONGO_PASSWORD", ""),
    }
    # Generate from: python -c 'import os; print(os.urandom(16))'
    SECRET_KEY = None


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
