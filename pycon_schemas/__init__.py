import json
import os

from .reader import read_schema


_schemas_path = os.path.join(os.path.dirname(__file__), 'schemas')

sponsor_schema = read_schema(os.path.join(_schemas_path, 'sponsor.json'))
sponsor_list_schema = read_schema(os.path.join(_schemas_path, 'sponsor_list.json'))
talk_schema = read_schema(os.path.join(_schemas_path, 'talk.json'))
