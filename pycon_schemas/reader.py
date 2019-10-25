import os
import json


def schemas_path():
    module_path = os.path.dirname(__file__)
    return os.path.join(module_path, 'schemas')


def get_schema(schema_name):
    schema_path = os.path.join(schemas_path(), f'{schema_name}.json')
    with open(schema_path) as f:
        schema = f.read()
    return json.loads(schema)
