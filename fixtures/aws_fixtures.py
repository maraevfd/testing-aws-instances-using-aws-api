"""Module contains fixtures for testing aws instance."""

import os
import pytest
from src.aws_wrappers.aws_instance import AWSInstance
from helpers.json_reader import read_expected_data


@pytest.fixture(scope='session')
def ec2_instance() -> AWSInstance:
    """Fixture returns an AWSInstance object for its further testing."""

    return AWSInstance(os.environ.get("INSTANCE_ID"), os.environ.get("REGION_NAME"))


@pytest.fixture(scope='session')
def expected_data(request) -> dict:
    """Fixture returns a dictionary that contains the expected data for testing AWSInstance."""
    path_to_project = request.config.args[0].partition('/tests')[0]
    return read_expected_data(os.path.join(path_to_project, 'helpers', 'expected_data.json'))
