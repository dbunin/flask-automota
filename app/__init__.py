#!flask/bin/python
from flask import Flask

app = Flask(__name__)
from app import views # Putting the import at the end avoid the circular import error