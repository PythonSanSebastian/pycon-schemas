import os
import json

import pytest
from jsonschema import validate

from pycon_schemas import talk_schema


@pytest.fixture
def examples_path():
    cwd = os.path.dirname(__file__)
    return os.path.join(cwd, 'examples')


@pytest.fixture
def talk_example(examples_path):
    with open(os.path.join(examples_path, 'talk.json')) as f:
        return json.load(f)


def test_talk_example_valid(talk_example):
    validate(instance=talk_example, schema=talk_schema)
