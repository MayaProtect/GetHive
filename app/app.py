import pymongo
import flask
from bson.binary import Binary
import json
from uuid import UUID
from flask_cors import CORS, cross_origin
from app.hive import Hive


class GetHive:
    def __init__(self, params):
        self.params = params
        self.app = flask.Flask(__name__)
        CORS(self.app)
        self.my_client = pymongo.MongoClient("mongodb://" + params['mongo_host'] + ":" + params['mongo_port'] + "/")
        self.db = self.my_client[params['mongo_db']]
        # Register routes
        #
        self.app.add_url_rule('/hive/<hive_id>', 'get_a_hive', self.get_a_hive, methods=['GET'])
        # Set CORS
        self.app.config['CORS_HEADERS'] = 'Content-Type'

    @cross_origin()
    def get_a_hive(self, hive_id) -> flask.Response:
        """
        Get a hive from DB and return it
        :return: Flask response
        """
        try:
            hive_id = UUID(hive_id)
        except ValueError:
            return flask.Response(status=400)
        coll = self.__get_collection()

        page_hive = coll.find_one({'uuid': Binary.from_uuid(hive_id)})
        if page_hive is None:
            return flask.Response(status=404)
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
