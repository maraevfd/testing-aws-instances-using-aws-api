"""Module contains fixtures for testing remote linux server."""

import logging
import os
import pytest
from helpers.env_variables import get_env_variable
from paramiko import AuthenticationException
from src.host_classes.linux_host import LinuxHost


@pytest.fixture(scope='session')
def host():
    """Fixture returns an LinuxHost object for its further testing."""

    try:
        return LinuxHost(get_env_variable("USER_NAME"),
                         get_env_variable("HOST_IP"),
                         os.path.expanduser(get_env_variable("PATH_TO_SSH_KEY")))
    except AuthenticationException:
        logging.error('Connection refused!')


@pytest.fixture(scope='session')
def cpu_number(host):
    """Fixture returns CPU cores number of the host server."""

    return host.get_cpu_cores_number()


@pytest.fixture(scope='session')
def network_interfaces_number(host):
    """Fixture returns CPU cores number of the host server."""

    return len(host.network_interfaces)


@pytest.fixture(scope='session')
def ram_size(host):
    """Fixture returns RAM size of the host server."""

    return host.get_ram_size()


@pytest.fixture(scope='session')
def partition_size(host):
    """Fixture returns partition size of the host server."""

    return host.get_partition_size()


@pytest.fixture(scope='session')
def chronyd_is_running(host):
    """Fixture returns True if chronyd is running."""

    return host.is_service_running('chronyd')


@pytest.fixture(scope='session')
def chronyd_is_enable(host):
    """Fixture returns True if chronyd is enable."""

    return host.is_service_enable('chronyd')
