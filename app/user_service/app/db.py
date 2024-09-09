import os
from dotenv import load_dotenv
from mongoengine import connect

load_dotenv()

HOST = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/smart-note')

def connect_db():
    connect(host=HOST)
    print("Connected to MongoDB.")