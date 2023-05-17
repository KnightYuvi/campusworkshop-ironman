"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi83v5269vf5qbdvtk0-a",
        database="dbironman",
        user="ironman",
        password="hKpBcG76oUFwFm0x8Bv9hWbOI5J1Y05A")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
