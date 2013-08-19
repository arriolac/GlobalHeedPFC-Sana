from flask import Flask
from flask_peewee.db import Database
from models import *
from flask_peewee.rest import RestAPI

DATABASE = {
        'name': 'openmrs',
        'engine': 'peewee.MySQLDatabase',
        'user': 'root',
        'passwd': 'GlobalHeedPFC1'
}
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

# Instantiate the DB wrapper
db = Database(app)

# Expose content via REST API
api = RestAPI(app)
api.register(Person)
api.setup()

if __name__ == '__main__':
    app.run()
