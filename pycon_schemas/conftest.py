import os
import json
import pytest

from jsonschema import Draft7Validator


@pytest.fixture
def examples_path():
    cwd = os.path.dirname(__file__)
    return os.path.join(cwd, 'tests', 'examples')


@pytest.fixture
def load_example(examples_path):
    def example_loader(example_file):
        with open(os.path.join(examples_path, example_file)) as f:
            return json.load(f)
    return example_loader


@pytest.fixture
def check_schema():
    return Draft7Validator.check_schema
