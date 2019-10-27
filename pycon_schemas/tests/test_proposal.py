import pytest

from pycon_schemas import proposal_schema


@pytest.fixture
def proposal_example(load_example):
    return load_example('proposal.json')


class TestProposalSchema:

    def test_proposal_schema_check(self, check_schema):
        check_schema(proposal_schema)

    def test_proposal_example_valid(self, validator, proposal_example):
        validator.validate(instance=proposal_example, schema=proposal_schema)
