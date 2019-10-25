import pytest

from pycon_schemas import speaker_schema


@pytest.fixture
def speaker_example(load_example):
    return load_example('speaker.json')


class TestSpeakerSchema:

    def test_speaker_schema_check(self, check_schema):
        check_schema(speaker_schema)

    def test_speaker_example_valid(self, validator, speaker_example):
        validator.validate(instance=speaker_example, schema=speaker_schema)
