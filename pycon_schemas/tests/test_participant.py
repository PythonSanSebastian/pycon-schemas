import pytest
from jsonschema import validate

from pycon_schemas import participant_schema


@pytest.fixture
def participant_example(load_example):
    return load_example('participant.json')


class TestParticipantSchema:

    def test_participant_schema_check(self, check_schema):
        check_schema(participant_schema)

    def test_participant_example_valid(self, validator, participant_example):
        validator.validate(instance=participant_example, schema=participant_schema)
