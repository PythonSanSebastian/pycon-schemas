import pytest

from pycon_schemas import participant_contact_schema


@pytest.fixture
def participant_contact_example(load_example):
    return load_example('participant_contact.json')


class TestParticipant_contactSchema:

    def test_participant_contact_schema_check(self, check_schema):
        check_schema(participant_contact_schema)

    def test_participant_contact_example_valid(self, validator, participant_contact_example):
        validator.validate(instance=participant_contact_example, schema=participant_contact_schema)
