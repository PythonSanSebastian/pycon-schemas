import pytest
from jsonschema import validate

from pycon_schemas import submission_schema


@pytest.fixture
def submission_example(load_example):
    return load_example('submission.json')


class TestSubmissionSchema:

    def test_submission_schema_check(self, check_schema):
        check_schema(submission_schema)

    def test_submission_example_valid(self, validator, submission_example):
        validator.validate(instance=submission_example, schema=submission_schema)
