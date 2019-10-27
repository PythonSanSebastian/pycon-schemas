import pytest

from pycon_schemas import sponsorship_schema


@pytest.fixture
def sponsorship_example(load_example):
    return load_example('sponsorship.json')


class TestSponsorListSchema:

    def test_sponsorship_schema_check(self, check_schema):
        check_schema(sponsorship_schema)

    def test_sponsorship_example_valid(self, validator, sponsorship_example):
        validator.validate(instance=sponsorship_example, schema=sponsorship_schema)
