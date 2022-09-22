
import pymongo
import flask
import json
import bson
from uuid import UUID, uuid4
from flask_cors import CORS, cross_origin
from os import environ as env


app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

# pour apres le function get_collection



def get_collection():
    my_client = pymongo.MongoClient('mongodb://' + env.get('MONGO_HOST') + ':' + env.get('MONGO_PORT') + '/')
    #my_client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
    db = my_client['mayaprotect']
    hive = db['hives']
    return hive


@app.route('/hive/<hive_id>', methods=['GET'])  
@cross_origin() 
# 打印所有蜂巢信息
def page_query(hive_id):
    args = flask.request.args
    #hive_id = args.get("uuid")
    hive_id = bson.Binary.from_uuid(UUID(hive_id))
    #station_id = args.get("stationId")
    
    coll = get_collection()
   # page_hive = coll.find()
    page_hive = coll.find_one({'uuid': hive_id})
    print(page_hive)
    rep = {
        'uuid': str(UUID(bytes=page_hive['uuid']))
       
    }
    
    
    return flask.Response(json.dumps(rep), mimetype='application/json')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)










  
