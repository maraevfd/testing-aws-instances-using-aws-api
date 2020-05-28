from src.aws_wrappers.aws_instance import AWSInstance
from helpers.json_reader import read_expected_data
import pytest


@pytest.fixture(scope='session')
def ec2_instance():
    ec2_instance = AWSInstance('i-06007db6d3063ca53', 'eu-central-1')
    return ec2_instance


@pytest.fixture(scope='session')
def expected_data():
    expected_data = read_expected_data()
    return expected_data
