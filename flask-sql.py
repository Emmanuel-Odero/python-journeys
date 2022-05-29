import imp
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://root:password@localhost:8080/mydb'
db = SQLAlchemy(app)

#person
class Person(db.Model):
    id = db.Column(db.Column)

@app.route('/')
def index():
    return 'Hello There'