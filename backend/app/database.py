from mongoengine import connect
import os

def connect_db():
    try:
        HOST = os.getenv('DATABASE_URI')
        connect(host=HOST)
        print("Connected to mongodb")
    except Exception as e:
        print(f'Failed to connect. \nError: \n\n{e}')