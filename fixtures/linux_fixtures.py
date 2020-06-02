"""Module contains fixtures for testing remote linux server."""

import logging
import os
import pytest
from helpers.env_variables import get_env_variable
from helpers.get_data_from_dict import get_receive_data
from src.host_classes.linux_host import LinuxHost
from typing import Optional


@pytest.fixture(scope='session')
def host() -> LinuxHost:
    """Fixture returns an LinuxHost object for its further testing."""

    return LinuxHost(get_env_variable("USER_NAME"),
                     get_env_variable("HOST_IP"),
                     os.path.expanduser(get_env_variable("PATH_TO_SSH_KEY")))


@pytest.fixture(scope='session')
def cpu_number(host: LinuxHost) -> int:
    """Fixture returns CPU cores number of the host server."""

    return host.get_cpu_cores_number()


@pytest.fixture(scope='session')
def network_interfaces_number(host: LinuxHost) -> int:
    """Fixture returns CPU cores number of the host server."""

    return len(host.network_interfaces)


@pytest.fixture(scope='session')
def ram_size(host: LinuxHost) -> int:
    """Fixture returns RAM size of the host server."""

    return host.get_ram_size()


@pytest.fixture(scope='session')
def partition_size(host: LinuxHost) -> int:
    """Fixture returns partition size of the host server."""

    return host.get_partition_size()


@pytest.fixture(scope='session')
def chronyd_is_running(host: LinuxHost) -> bool:
    """Fixture returns True if chronyd is running."""

    return host.is_service_running('chronyd')


@pytest.fixture(scope='session')
def chronyd_is_enable(host: LinuxHost) -> bool:
    """Fixture returns True if chronyd is enable."""

    return host.is_service_enable('chronyd')


@pytest.fixture(scope='session')
def expected_cpu_number(expected_data: dict) -> Optional[int]:
    """Fixture returns the expected minimum number of processor cores."""

    return get_receive_data(expected_data,
                            "cpu_cores_number",
                            'The expected number of processor cores is not indicated in the file!')


@pytest.fixture(scope='session')
def expected_network_interfaces_number(expected_data: dict) -> Optional[int]:
    """Fixture returns the expected minimum number of host network interfaces."""

    return get_receive_data(expected_data,
                            "net_interfaces_number",
                            'The expected number of network interfaces is not indicated in the file!')


@pytest.fixture(scope='session')
def expected_ram_size(expected_data: dict) -> Optional[int]:
    """Fixture returns the expected minimum host RAM size."""

    return get_receive_data(expected_data,
                            "ram_size",
                            'The expected RAM size is not indicated in the file!')


@pytest.fixture(scope='session')
def expected_partition_size(expected_data: dict) -> Optional[int]:
    """Fixture returns the expected minimum host partition size."""

    return get_receive_data(expected_data,
                            "partition_size",
                            'The expected minimum partition size is not indicated in the file!')


@pytest.fixture(scope='session')
def expected_chronyd_is_running(expected_data: dict) -> Optional[bool]:
    """Fixture returns the expected boolean chronyd is running."""

    return get_receive_data(expected_data,
                            "is_chronyd_running",
                            'The expected status of chronyd is not indicated in the file!')


@pytest.fixture(scope='session')
def expected_chronyd_is_enable(expected_data: dict) -> Optional[bool]:
    """Fixture returns the expected boolean chronyd is enable."""

    return get_receive_data(expected_data,
                            "is_chronyd_enable",
                            'The expected status of chronyd is not indicated in the file!')
