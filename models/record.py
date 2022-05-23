from datetime import datetime
from enum import Enum
from pydantic import BaseModel

class OperationEnum(str, Enum):
    create = "create"
    update = "update"
    patch = "patch"
    delete = "delete"

class Record(BaseModel):
    application: str
    resource_type: str
    operator: str
    operation: OperationEnum
    record_time: datetime=datetime.now()
    obj_identifier: str="uuid"
    obj_content: dict

EXAMPLES = {
    "role": {
        "value": {
            "application": "rbac",
            "resource_type": "role",
            "operator": "zhzeng",
            "operation": "create",
            "obj_content": {
                "uuid": "4df211e0-2d88-49a4-8802-728630224d15",
                "name": "RoleTest",
                "access": [
                    {
                        "permission": "app:*:read",
                        "resourceDefinitions": [
                            {
                                "attributeFilter": {
                                    "key": "app.attribute.case",
                                    "operation": "equal",
                                    "value": "thevalue"
                                }
                            }
                        ]
                    }
                ]
            }
        }
    },
    "group": {
        "value": {
            "application": "rbac",
            "resource_type": "group",
            "operator": "zhzeng",
            "operation": "create",
            "obj_content": {
                "uuid": "16fd2706-8baf-433b-82eb-8c7fada847da",
                "name": "test",
                "principals": [
                                { "username": "zhzeng" }
                            ],
                "roles": [
                    {
                        "name": "RoleTest",
                        "uuid": "4df211e0-2d88-49a4-8802-728630224d15"
                    }
                ]
            }
        }
    }
}

