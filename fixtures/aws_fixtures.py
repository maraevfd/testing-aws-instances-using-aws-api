"""Module contains fixtures for testing aws instance."""

import logging
import pytest
from helpers.env_variables import get_env_variable
from helpers.get_data_from_dict import get_receive_data
from src.aws_wrappers.aws_instance import AWSInstance
from typing import Optional


@pytest.fixture(scope='session')
def ec2_instance() -> AWSInstance:
    """Fixture returns an AWSInstance object for its further testing."""

    return AWSInstance(get_env_variable("INSTANCE_ID"), get_env_variable("REGION_NAME"))


@pytest.fixture(scope='session')
def ec2_network_interface_number(ec2_instance: AWSInstance) -> int:
    """Fixture returns an AWSInstance network interfaces number."""

    return len(ec2_instance.get_network_interfaces())


@pytest.fixture(scope='session')
def ec2_tags_number(ec2_instance: AWSInstance) -> int:
    """Fixture returns an AWSInstance tags number."""

    return len(ec2_instance.tags)


@pytest.fixture(scope='session')
def ec2_tag_name_value(ec2_instance: AWSInstance) -> Optional[str]:
    """Fixture returns an AWSInstance object tag name value."""

    return get_receive_data(ec2_instance.tags,
                            'Name',
                            'KeyError in instance tags! Check tag "Name".')


@pytest.fixture(scope='session')
def expected_ec2_state(expected_data: dict) -> Optional[str]:
    """Fixture returns the expected instance state."""

    return get_receive_data(expected_data,
                            "state",
                            'The expected instance state is not indicated in the file!')


@pytest.fixture(scope='session')
def expected_ec2_type(expected_data: dict) -> Optional[str]:
    """Fixture returns the expected instance type."""

    return get_receive_data(expected_data,
                            "type",
                            'The expected instance type is not indicated in the file!')


@pytest.fixture(scope='session')
def expected_net_interface_num(expected_data: dict) -> Optional[int]:
    """Fixture returns the expected network interfaces number of the instance."""

    return get_receive_data(expected_data,
                            "net_interfaces_number",
                            'The expected network interfaces number is not indicated in the file!')


@pytest.fixture(scope='session')
def expected_tags_number(expected_data: dict) -> Optional[int]:
    """Fixture returns the expected tags number of the instance."""

    return get_receive_data(expected_data,
                            "tags_number",
                            'The expected instance tags number is not indicated in the file!')


@pytest.fixture(scope='session')
def expected_tag_name(expected_data: dict) -> Optional[str]:
    """Fixture returns the expected tag name value of the instance."""

    return get_receive_data(expected_data,
                            "tag_name",
                            'The expected tag name is not indicated in the file!')


@pytest.fixture(scope='session')
def expected_ec2_key_name(expected_data: dict) -> Optional[str]:
    """Fixture returns the expected ssh key name of the instance."""

    return get_receive_data(expected_data,
                            "ssh_key_name",
                            'The expected ssh key name is not indicated in the file!')


@pytest.fixture(scope='session')
def expected_root_device(expected_data: dict) -> Optional[str]:
    """Fixture returns the expected root device type of the instance."""

    return get_receive_data(expected_data,
                            "root_device_type",
                            'The expected root device type is not indicated in the file!')


@pytest.fixture(scope='session')
def expected_volume_size(expected_data: dict) -> Optional[int]:
    """Fixture returns the expected minimum EBSVolume size of the instance."""

    return get_receive_data(expected_data,
                            "ebs_size",
                            'The expected instance EBS size is not indicated in the file!')


@pytest.fixture(scope='session')
def expected_private_ip(expected_data: dict) -> Optional[str]:
    """Fixture returns the expected network interface private IP of the instance."""

    return get_receive_data(expected_data,
                            "private_ip",
                            'The expected private IP is not indicated in the file!')


@pytest.fixture(scope='session')
def expected_public_ip(expected_data: dict) -> Optional[str]:
    """Fixture returns the expected network interface public IP of the instance."""

    return get_receive_data(expected_data,
                            "public_ip",
                            'The expected public IP is not indicated in the file!')
