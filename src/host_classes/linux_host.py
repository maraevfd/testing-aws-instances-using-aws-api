"""The module contains the LinuxHost class and its attributes."""

import testinfra


class LinuxHost:
    """The class provides an interface for obtaining information about a linux server."""

    def __init__(self, username: str, ip_address: str, path_to_ssh_key: str):
        """
        :param username: Username for connection to the server.
        :param ip_address: Ip address of the remote server.
        :param path_to_ssh_key: Full path to file with private ssh key.
        """

        self.backend = 'paramiko://' + username + '@' + ip_address
        self.host = testinfra.get_host(self.backend, ssh_identity_file=path_to_ssh_key)

    def get_cpu_cores_number(self) -> int:
        """Method returns CPU cores number of the linux server. Example: 1"""

        return int(self.host.run("nproc").stdout)

    def get_ram_size(self) -> int:
        """Method returns RAM size (Mb) of the linux server. Example: 938"""

        return int(self.host.run("free -m | grep Mem | awk '{print $2}'").stdout)

    def get_network_interfaces(self) -> list:
        """Method returns a list with names of network interfaces of the server. Example: ['enp0s3', 'lo']"""

        return self.host.run('ls -A /sys/class/net').stdout.split()

    def get_partition_size(self) -> int:
        """Method returns partition size (Gb) of the linux server. Example: 938"""

        return int(self.host.run("lsblk | grep disk | awk '{print $4}'").stdout.replace('G', ''))

    def is_chronyd_running(self) -> bool:
        """Method returns True if chronyd is running"""

        return self.host.service('chronyd').is_running

    def is_chronyd_enable(self) -> bool:
        """Method returns True if chronyd is enabled"""

        return self.host.service('chronyd').is_enabled
