import pytest
from jsonschema import validate

from pycon_schemas import sponsor_contact_schema


@pytest.fixture
def sponsor_contact_example(load_example):
    return load_example('sponsor_contact.json')


class TestSponsorContactSchema:

    def test_sponsor_contact_schema_check(self, check_schema):
        check_schema(sponsor_contact_schema)

    def test_sponsor_contact_example_valid(self, validator, sponsor_contact_example):
        validator.validate(instance=sponsor_contact_example, schema=sponsor_contact_schema)
