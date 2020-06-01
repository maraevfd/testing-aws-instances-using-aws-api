"""Module contains fixtures for testing aws instance."""

import pytest
from src.aws_wrappers.aws_instance import AWSInstance
from helpers.env_variables import get_env_variable


@pytest.fixture(scope='session')
def ec2_instance() -> AWSInstance:
    """Fixture returns an AWSInstance object for its further testing."""

    return AWSInstance(get_env_variable("INSTANCE_ID"), get_env_variable("REGION_NAME"))
