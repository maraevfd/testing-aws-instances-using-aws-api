"""Module contains fixtures for testing remote linux server."""

import pytest
from src.host_classes.linux_host import LinuxHost


@pytest.fixture(scope='session')
def host():
    """Fixture returns an LinuxHost object for its further testing."""

    return LinuxHost('ec2-user', '18.156.5.31', '/home/fedor/.ssh/jenkins_access')
