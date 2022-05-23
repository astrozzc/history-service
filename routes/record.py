from fastapi import APIRouter, Body

from models.record import EXAMPLES, Record
from config.db import conn
from schema.record import recordEntity, records
from bson import ObjectId

record = APIRouter()

@record.get("/", response_model=list[Record])
async def find_all_records():
    return records(conn.local.record.find())

@record.get("/{record_id}")
async def find_record_of_obj(record_id):
    return recordEntity(conn.local.record.find_one({"_id":ObjectId(record_id)}))

@record.post("/", response_model=Record)
async def create_record(record: Record=Body(examples=EXAMPLES)):
    record_obj = conn.local.record.insert_one(dict(record))
    record_id = record_obj.inserted_id
    return recordEntity(conn.local.record.find_one({"_id":record_id}))

@record.get("/history/{object_id}", response_model=list[Record])
async def object_history(object_id, app, resource, identifier="uuid"):
    return records(conn.local.record.find({"$and":[{"application":app}, {"resource_type": resource}, {f"obj_content.{identifier}":object_id}]}))