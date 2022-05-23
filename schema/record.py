def recordEntity(item) -> dict:
    item['_id'] = str(item['_id'])
    return item

def records(entity) -> list:
    return [recordEntity(item) for item in entity]