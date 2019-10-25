import pytest
from jsonschema import validate

from pycon_schemas import sponsor_schema


@pytest.fixture
def sponsor_example(load_example):
    return load_example('sponsor.json')


class TestSponsorSchema:

    def test_sponsor_schema_check(self, check_schema):
        check_schema(sponsor_schema)

    def test_sponsor_example_valid(self, validator, sponsor_example):
        validator.validate(instance=sponsor_example, schema=sponsor_schema)
