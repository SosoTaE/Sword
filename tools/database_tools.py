from pymongo import MongoClient

def initialize_database(connection_string, database_name, collection_name):
    client = MongoClient(connection_string)
    print(database_name)
    db = client[database_name]
    collection = db[collection_name]

    return collection