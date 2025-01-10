from pymongo import MongoClient

def get_database():
    """Connect to MongoDB and return the database object."""
    client = MongoClient("mongodb://localhost:27017/")
    return client['posDB']