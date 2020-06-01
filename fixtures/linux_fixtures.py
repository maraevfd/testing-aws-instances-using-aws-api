"""Module contains fixtures for testing remote linux server."""

import logging
import os
import pytest
import socket
from fixtures.general_fixtures import expected_data
from helpers.env_variables import get_env_variable
from paramiko import AuthenticationException
from src.host_classes.linux_host import LinuxHost
from typing import Optional


@pytest.fixture(scope='session')
def host():
    """Fixture returns an LinuxHost object for its further testing."""

    try:
        return LinuxHost(get_env_variable("USER_NAME"),
                         get_env_variable("HOST_IP"),
                         os.path.expanduser(get_env_variable("PATH_TO_SSH_KEY")))
    except (AuthenticationException, socket.timeout):
        logging.error('Connection refused!')


@pytest.fixture(scope='session')
def cpu_number(host) -> int:
    """Fixture returns CPU cores number of the host server."""

    return host.get_cpu_cores_number()


@pytest.fixture(scope='session')
def network_interfaces_number(host) -> int:
    """Fixture returns CPU cores number of the host server."""

    return len(host.network_interfaces)


@pytest.fixture(scope='session')
def ram_size(host) -> int:
    """Fixture returns RAM size of the host server."""

    return host.get_ram_size()


@pytest.fixture(scope='session')
def partition_size(host) -> int:
    """Fixture returns partition size of the host server."""

    return host.get_partition_size()


@pytest.fixture(scope='session')
def chronyd_is_running(host) -> bool:
    """Fixture returns True if chronyd is running."""

    return host.is_service_running('chronyd')


@pytest.fixture(scope='session')
def chronyd_is_enable(host) -> bool:
    """Fixture returns True if chronyd is enable."""

    return host.is_service_enable('chronyd')


@pytest.fixture(scope='session')
def expected_cpu_number(expected_data: dict) -> Optional[int]:
    """Fixture returns the expected minimum number of processor cores."""

    if expected_data.get("cpu_cores_number"):
        return expected_data.get("cpu_cores_number")
    logging.error('The expected number of processor cores is not indicated in the file!')
    return None


@pytest.fixture(scope='session')
def expected_network_interfaces_number(expected_data: dict) -> Optional[int]:
    """Fixture returns the expected minimum number of host network interfaces."""

    if expected_data.get("net_interfaces_number"):
        return expected_data.get("net_interfaces_number")
    logging.error('The expected number of network interfaces is not indicated in the file!')
    return None


@pytest.fixture(scope='session')
def expected_ram_size(expected_data: dict) -> Optional[int]:
    """Fixture returns the expected minimum host RAM size."""

    if expected_data.get("ram_size"):
        return expected_data.get("ram_size")
    logging.error('The expected RAM size is not indicated in the file!')
    return None


@pytest.fixture(scope='session')
def expected_partition_size(expected_data: dict) -> Optional[int]:
    """Fixture returns the expected minimum host partition size."""

    if expected_data.get("partition_size"):
        return expected_data.get("partition_size")
    logging.error('The expected minimum partition size is not indicated in the file!')
    return None


@pytest.fixture(scope='session')
def expected_chronyd_is_running(expected_data: dict) -> Optional[bool]:
    """Fixture returns the expected boolean chronyd is running."""

    if expected_data.get("is_chronyd_running") or False:
        return expected_data.get("is_chronyd_running")
    logging.error('The expected status of chronyd is not indicated in the file!')
    return None


@pytest.fixture(scope='session')
def expected_chronyd_is_enable(expected_data: dict) -> Optional[bool]:
    """Fixture returns the expected boolean chronyd is enable."""

    if expected_data.get("is_chronyd_enable") or False:
        return expected_data.get("is_chronyd_enable")
    logging.error('The expected status of chronyd is not indicated in the file!')
    return None
