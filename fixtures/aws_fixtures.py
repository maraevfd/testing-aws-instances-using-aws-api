"""Module contains fixtures for testing aws instance."""

import logging
import pytest
from botocore.exceptions import ClientError
from helpers.env_variables import get_env_variable
from src.aws_wrappers.aws_instance import AWSInstance
from typing import Optional


@pytest.fixture(scope='session')
def ec2_instance() -> Optional[AWSInstance]:
    """Fixture returns an AWSInstance object for its further testing."""

    try:
        return AWSInstance(get_env_variable("INSTANCE_ID"), get_env_variable("REGION_NAME"))
    except ClientError:
        logging.error('Unable to retrieve the AWSInstance object, please check the connection!')
        return None


@pytest.fixture(scope='session')
def ec2_network_interface_number(ec2_instance: AWSInstance) -> Optional[int]:
    """Fixture returns an AWSInstance network interfaces number."""

    try:
        return len(ec2_instance.network_interfaces)
    except TypeError:
        logging.error('Invalid data type received! Check the list of instance network interfaces.')
        return None


@pytest.fixture(scope='session')
def ec2_tags_number(ec2_instance: AWSInstance) -> Optional[int]:
    """Fixture returns an AWSInstance tags number."""

    try:
        return len(ec2_instance.tags)
    except TypeError:
        logging.error('Invalid data type received! Check the list of instance tags.')
        return None


@pytest.fixture(scope='session')
def ec2_tag_name_value(ec2_instance: AWSInstance) -> Optional[str]:
    """Fixture returns an AWSInstance object tag name value."""

    try:
        return ec2_instance.tags['Name']
    except KeyError:
        logging.error('KeyError in instance tags! Check tag "Name".')
        return None


@pytest.fixture(scope='session')
def expected_ec2_state(expected_data: dict) -> Optional[str]:
    """Fixture returns the expected instance state."""

    if expected_data.get("state"):
        return expected_data.get("state")
    logging.error('The expected instance state is not indicated in the file!')
    return None


@pytest.fixture(scope='session')
def expected_ec2_type(expected_data: dict) -> Optional[str]:
    """Fixture returns the expected instance type."""

    if expected_data.get("type"):
        return expected_data.get("type")
    logging.error('The expected instance type is not indicated in the file!')
    return None


@pytest.fixture(scope='session')
def expected_net_interface_num(expected_data: dict) -> Optional[int]:
    """Fixture returns the expected network interfaces number of the instance."""

    if expected_data.get("net_interfaces_number"):
        return expected_data.get("net_interfaces_number")
    logging.error('The expected network interfaces number is not indicated in the file!')
    return None


@pytest.fixture(scope='session')
def expected_tags_number(expected_data: dict) -> Optional[int]:
    """Fixture returns the expected tags number of the instance."""

    if expected_data.get("tags_number"):
        return expected_data.get("tags_number")
    logging.error('The expected instance tags number is not indicated in the file!')
    return None


@pytest.fixture(scope='session')
def expected_tag_name(expected_data: dict) -> Optional[str]:
    """Fixture returns the expected tag name value of the instance."""

    if expected_data.get("tag_name"):
        return expected_data.get("tag_name")
    logging.error('The expected tag name is not indicated in the file!')
    return None


@pytest.fixture(scope='session')
def expected_ec2_key_name(expected_data: dict) -> Optional[str]:
    """Fixture returns the expected ssh key name of the instance."""

    if expected_data.get("ssh_key_name"):
        return expected_data.get("ssh_key_name")
    logging.error('The expected ssh key name is not indicated in the file!')
    return None


@pytest.fixture(scope='session')
def expected_root_device(expected_data: dict) -> Optional[str]:
    """Fixture returns the expected root device type of the instance."""

    if expected_data.get("root_device_type"):
        return expected_data.get("root_device_type")
    logging.error('The expected root device type is not indicated in the file!')
    return None


@pytest.fixture(scope='session')
def expected_volume_size(expected_data: dict) -> Optional[int]:
    """Fixture returns the expected minimum EBSVolume size of the instance."""

    if expected_data.get("ebs_size"):
        return expected_data.get("ebs_size")
    logging.error('The expected instance EBS size is not indicated in the file!')
    return None


@pytest.fixture(scope='session')
def expected_private_ip(expected_data: dict) -> Optional[str]:
    """Fixture returns the expected network interface private IP of the instance."""

    if expected_data.get("private_ip"):
        return expected_data.get("private_ip")
    logging.error('The expected private IP is not indicated in the file!')
    return None


@pytest.fixture(scope='session')
def expected_public_ip(expected_data: dict) -> Optional[str]:
    """Fixture returns the expected network interface public IP of the instance."""

    if expected_data.get("public_ip"):
        return expected_data.get("public_ip")
    logging.error('The expected public IP is not indicated in the file!')
    return None
