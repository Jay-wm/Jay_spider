from pymongo import MongoClient

# Initialize the database, client.string means a database called string is created.
client = MongoClient()


""" Main function, looking  db_c as db.collection_name in MongoDB"""
# dbc means db.collection_name in the MongoDB.
databases_name = ['chapter6_1']
collections_name = ['collection_name1']
db = client[databases_name[0]]
db_c = db[collections_name[0]]


doc1 = {"name":"kingname", "age":18, "salary":99999}
db_c.insert(doc1)
    
