import pytest

from pycon_schemas import presentation_schema


@pytest.fixture
def presentation_example(load_example):
    return load_example('presentation.json')


class TestPresentationSchema:

    def test_presentation_schema_check(self, check_schema):
        check_schema(presentation_schema)

    def test_presentation_example_valid(self, validator, presentation_example):
        validator.validate(instance=presentation_example, schema=presentation_schema)
