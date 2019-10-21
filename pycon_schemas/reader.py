import os
import json


def read_schema(schema_path):
    with open(schema_path) as f:
        schema = f.read()
    return json.loads(schema)
