from pymongo import MongoClient
import pandas as pd
import json


def import_csvfile():
    client = MongoClient('mongodb://cos-tccc-ebt-dev:agbi8w1dIVykarU9z8Kf0bwGEMnyS4LW9iWRA7gYsJoLjQpUGjQUNkZsWhehjQ1CSLoapF0xgXK5p8NUAlpN6g==@cos-tccc-ebt-dev.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@cos-tccc-ebt-dev@', retrywrites=False)
    mng_db = client['EnrichmentDocs']  # Replace mongo db name
    collection_name = 'NielsenData'  # Replace mongo db collection name
    db_cm = mng_db[collection_name]
    data = pd.read_csv('output-local.csv')
    data['quarter'] = 'q4'
    data_json = json.loads(data.to_json(orient='records'))
    db_cm.insert(data_json)

import_csvfile()