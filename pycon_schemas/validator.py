from jsonschema import Draft7Validator, RefResolver

from .reader import schemas_path


pycon_schema_resolver = RefResolver('file://' + schemas_path(), None)


class PyconSchemaValidator(Draft7Validator):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, resolver=pycon_schema_resolver, **kwargs)
