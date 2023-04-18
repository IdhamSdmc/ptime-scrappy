from pymongo import MongoClient
import configparser
from pymongo.server_api import ServerApi

config = configparser.ConfigParser()
config.read('sample.ini')
uri = config.get('PROD', 'DB_URI')
uri = "mongodb+srv://idanniel:WFsdMDSEUclo7ykU@cluster007.phfg7kl.mongodb.net/?retryWrites=true&w=majority"
conn = MongoClient(uri, server_api=ServerApi('1'))
db = conn.get_database('senahmi')
collection = db.get_collection('time_pronostico')


