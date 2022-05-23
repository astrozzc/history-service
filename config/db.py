from pymongo import MongoClient
import os

mdb_url = os.environ.get("MDB_URL") or "mongodb://root:root1234@mongodb:27017/?authMechanism=DEFAULT"

conn = MongoClient(mdb_url)