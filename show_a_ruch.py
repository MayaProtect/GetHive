
 
import pymongo
import flask
import json
from flask_cors import CORS, cross_origin
import os


app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

# pour apres le function get_collection



def get_collection():
    my_client = pymongo.MongoClient('mongodb://' + os.environ["MONGO_HOST"] + ':' + os.environ["MONGO_PORT"] + '/')
    db = my_client.list_database_names()
    hive = db.hive
    return hive


@app.route('/hive', methods=['GET'])  
@cross_origin() 
# 打印所有蜂巢信息
def page_query():
    args = flask.request.args
    hive_id = args.get("id")
    station_id = args.get("stationId")
    
    coll = get_collection()
    page_hive = coll.find(hive_id)
    
    return flask.Response(json.dumps(page_hive), mimetype='application/json')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)










  
