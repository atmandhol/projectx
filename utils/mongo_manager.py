import sys
import logging
import pymongo
import traceback


# Requires pymongo==3.6.0
class MongoManager:
    def __init__(self, logger=None, uri=None, host="localhost", port=27017, use_uri=True, db="test_db",
                 collection="test_collection"):
        if not logger:
            self.logger = logging.getLogger("Mongo Logger")
            self.logger.setLevel(logging.DEBUG)
            logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
        else:
            self.logger = logger

        if use_uri:
            self.client = pymongo.MongoClient(uri)
        else:
            self.client = pymongo.MongoClient(host=host, port=port)

        self.db = self.client[db]
        self.collection = self.db[collection]

    def insert_one(self, document):
        """
        Inserts a document into Mongo
        :param document: (Dict) Mongo Document
        :return: (String) _id of the inserted document
        """
        try:
            return self.collection.insert_one(document=document).inserted_id
        except Exception:
            self.logger.error("Error inserting one object to mongo. Traceback: %s" % str(traceback.format_exc(1)))
            return None

    def find_one(self):
        """
        Returns a random document from a collection
        :return: (Dict)
        """
        try:
            return self.collection.find_one()
        except Exception:
            self.logger.error("Error finding one object from mongo. Traceback: %s" % str(traceback.format_exc(1)))
            return None

    def find_by_id(self, id):
        """
        Returns the document matching that _id
        :param id: (String) _id
        :return: (Dict) if found, None is not Found
        """
        try:
            return self.collection.find_one({"_id": id})
        except Exception:
            self.logger.error("Error finding object from mongo. Traceback: %s" % str(traceback.format_exc(1)))
            return None

    def get_all(self, max_docs=0):
        """
        Returns a list of all docs
        :return:
        """
        try:
            docs = list()
            result = self.collection.find({}).limit(max_docs)
            for entry in result:
                docs.append(entry)

            return docs
        except Exception:
            self.logger.error("Error finding object from mongo. Traceback: %s" % str(traceback.format_exc(1)))
            return None

    def query(self, query):
        """
        Query using proper query dictionary
        :param query:
        :return: (list) of documents. returns [] if no match
        """
        try:
            docs = list()
            result = self.collection.find(query)
            for entry in result:
                docs.append(entry)

            return docs
        except Exception:
            self.logger.error("Error finding objects from mongo. Traceback: %s" % str(traceback.format_exc(1)))
            return None

    def save(self, document):
        """
        Returns _id of the Saved document
        :param document: (Dict) JSON containing the _id field
        :return:
        """
        try:
            return self.collection.save(document, manipulate=True)
        except Exception:
            self.logger.error("Error saving object to mongo. Traceback: %s" % str(traceback.format_exc(1)))
            return None