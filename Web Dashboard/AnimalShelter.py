from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure

class AnimalShelter(object):
	def __init__(self, username='aacuser', password='SNHU1234', host='nv-desktop-services.apporto.com', port=32818, db='AAC', col='animals'):
		try:
			self.client = MongoClient(f"mongodb://{username}:{password}@{host}:{port}/?authSource=admin")
			self.database = self.client[db]
			self.collection = self.database[col]
			print("Successfully connected to MongoDB!")
		except ConnectionFailure as e:
			print("Could not connect to MongoDB: ", e)
			raise
	def create(self, data):
		if data is not None and isinstance(data, dict):
			try:
				result = self.collection.insert_one(data)
				return True if result.inserted_id else False
			except OperationFailure as e:
				print("Insert Failed: ", e)
				return False
		else:
			raise Exception("Data is invalid. Must be a non-empty dictionary")

	def read(self, query):
		if query is not None and isinstance(query, dict):
			try:
				results = list(self.collection.find(query))
				return results
			except OperationFailure as e:
				print ("Read Failed: ", e)
				return []
		else:
			raise Exception("Invalid Query: must be a non-empty dictionary")

	def update(self, query, new_values):
    		if query and new_values:
        		try:
            			result = self.collection.update_many(query, {"$set": new_values})
            			return result.modified_count  # Number of documents updated
        		except Exception as e:
            			print("Update Failed:", e)
            			return 0
    		else:
        		raise Exception("Query and update values must be non-empty dictionaries")

# Delete method to implement the D in CRUD
	def delete(self, query):
    		if query:
        		try:
            			result = self.collection.delete_many(query)
            			return result.deleted_count  # Number of documents deleted
        		except Exception as e:
            			print("Delete Failed:", e)
            			return 0
    		else:
        		raise Exception("Query must be a non-empty dictionary")
