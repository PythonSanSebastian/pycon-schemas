import os
import json
import pytest

from jsonschema import Draft7Validator, RefResolver

import pycon_schemas


@pytest.fixture
def examples_path():
    cwd = os.path.dirname(__file__)
    return os.path.join(cwd, 'tests', 'examples')


@pytest.fixture
def schemas_path():
    module_path = os.path.dirname(pycon_schemas.__file__)
    return os.path.join(module_path, 'schemas')


@pytest.fixture
def load_example(examples_path):
    def example_loader(example_file):
        with open(os.path.join(examples_path, example_file)) as f:
            return json.load(f)
    return example_loader


@pytest.fixture
def check_schema():
    return Draft7Validator.check_schema


@pytest.fixture
def validator(schemas_path):
    class JsonSchemaValidator:

        def __init__(self, resolver):
            self.resolver = resolver

        def validate(self, instance, schema):
            validator = Draft7Validator(schema=schema, resolver=self.resolver)
            return validator.validate(instance)

    resolver = RefResolver('file://' + schemas_path, None)
    return JsonSchemaValidator(resolver)
