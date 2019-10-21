import pytest
from jsonschema import validate

from pycon_schemas import sponsor_list_schema


@pytest.fixture
def sponsor_list_example(load_example):
    return load_example('sponsor_list.json')


class TestSponsorListSchema:

    def test_sponsor_list_schema_check(self, check_schema):
        check_schema(sponsor_list_schema)

    def test_sponsor_example_valid(self, sponsor_list_example):
        validate(instance=sponsor_list_example, schema=sponsor_list_schema)
