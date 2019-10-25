import os
from jsonschema import Draft7Validator, RefResolver

from .reader import schemas_path


pycon_schema_resolver = RefResolver('file://' + schemas_path(), None)


class PyconSchemaValidator(Draft7Validator):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, resolver=pycon_schema_resolver, **kwargs)


# class PyconSchemaValidator:

#     def __init__(self):
#         self.resolver = PyconSchemaResolver

#     def validate(self, instance, schema):
#         validator = Draft7Validator(schema=schema, resolver=self.resolver)
#         return validator.validate(instance)

