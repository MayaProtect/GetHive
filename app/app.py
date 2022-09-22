import pymongo
import flask
import bson
import json
from uuid import UUID
from flask_cors import CORS, cross_origin
from hive import Hive 


class GetHive:
    def __init__(self, params):
        self.params = params
        self.app = flask.Flask(__name__)
        CORS(self.app)
        self.my_client = pymongo.MongoClient("mongodb://" + params['mongo_host'] + ":" + params['mongo_port'] + "/")
        self.db = self.my_client[params['mongo_db']]
        self.default_limit = params['default_limit']
        # Register routes
        #
        self.app.add_url_rule('/hive/<hive_id>', 'get_a_hive', self.get_a_hive, methods=['GET'])
        # Set CORS
        self.app.config['CORS_HEADERS'] = 'Content-Type'

    @cross_origin()
    def get_a_hive(self) -> flask.Response:
        """
        Get a hive from DB and return it
        :return: Flask response
        """
        args = flask.request.args
        
        #!!!!!!!!!!!!!!!!!!!!!!
        hive_id = bson.Binary.from_uuid(UUID(hive_id))
        coll = self.__get_collection()

        page_hive = coll.find_one({'uuid': hive_id})
        print(page_hive)
        hive= Hive(page_hive)
        rep = hive.__to_json__()
        
        return flask.Response(json.dumps(rep), mimetype='application/json')
        

       

    def __get_collection(self) -> pymongo.collection.Collection:
        """
        :return: MongoDB collection
        """
        hives = self.db['hives']
        return hives

 

    def run(self) -> None:
        """
        Run Flask app
        """
        self.app.run(host='0.0.0.0', port=8080)
