from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'password'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31765
        DB = 'AAC'
        COL = 'animals'
        
        #
        # Initialize Connection
        #
        try:
            self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
            self.database = self.client['%s' % (DB)]
            self.collection = self.database['%s' % (COL)]
            print("Connection to MongoDB Successful")
        except errors.ConnectionError as e:
            print(f"Could not connect to MongoDB: {e}")
            
        username = USER
        password = PASS

        # Create method to implement the C in CRUD.
    def create(self, data):
            """
            This method inserts a new document into the 'animals' collection.

            Parameters:
            data (dict): The data to be inserted into the collection. This should be a dictionary.

            Returns:
            str: A success message indicating the insertion was successful.

            Raises:
            Exception: If the data parameter is None or empty.
            """
            if data is not None:
                result = self.database.animals.insert_one(
                    data)  # Insert the dictionary 'data' into the 'animals' collection
                return True if result.acknowledged else False
            else:
                raise Exception("Nothing to save, because data parameter is empty")

        # Read method to implement the R in CRUD.
    def read(self, query):
            """
            This method retrieves documents from the 'animals' collection that match the specified query.

            Parameters:
            query (dict): The query to filter the documents in the collection. This should be a dictionary.

            Returns:
            list: A list of documents that match the query.

            Raises:
            Exception: If the query parameter is None or empty.
            """
            if query is not None:
                return list(self.database.animals.find(query))  # Find and return documents matching the query
            else:
                raise Exception("Nothing to read, because query parameter is empty")

    def update(self, query, new_values):
            """
            This method updates documents in the 'animals' collection that match the specified query.

            Parameters:
            query (dict): The query to filter the documents in the collection. This should be a dictionary.
            new_values (dict): The new values to update the matching documents. This should be a dictionary in the format {'$set': {...}}.

            Returns:
            int: The number of documents modified.

            Raises:
            Exception: If the query or new_values parameter is None or empty.
            """
            if query is not None and new_values is not None:
                result = self.database.animals.update_many(query, new_values)  # Update documents matching the query
                return result.modified_count  # Return the number of documents modified
            else:
                raise Exception("Query and new values must be provided")

    def delete(self, query):
            """
            This method deletes documents from the 'animals' collection that match the specified query.

            Parameters:
            query (dict): The query to filter the documents in the collection. This should be a dictionary.

            Returns:
            int: The number of documents deleted.

            Raises:
            Exception: If the query parameter is None or empty.
            """
            if query is not None:
                result = self.database.animals.delete_many(query)  # Delete documents matching the query
                return result.deleted_count  # Return the number of documents deleted
            else:
                raise Exception("Query parameter must be provided")
