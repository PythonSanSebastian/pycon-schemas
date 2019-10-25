import os
import json

import pytest
from jsonschema import validate

from pycon_schemas import talk_schema


@pytest.fixture
def talk_example(load_example):
    return load_example('talk.json')


class TestTalkSchema:

    def test_talk_schema_check(self, check_schema):
        check_schema(talk_schema)

    def test_talk_example_valid(self, validator, talk_example):
        validator.validate(instance=talk_example, schema=talk_schema)
