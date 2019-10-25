import pytest

from pycon_schemas import sponsorships_schema


@pytest.fixture
def sponsorships_example(load_example):
    return load_example('sponsorships.json')


class TestSponsorListSchema:

    def test_sponsorships_schema_check(self, check_schema):
        check_schema(sponsorships_schema)

    def test_sponsorships_example_valid(self, validator, sponsorships_example):
        validator.validate(instance=sponsorships_example, schema=sponsorships_schema)
