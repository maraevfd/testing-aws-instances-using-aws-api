"""The module contains the LinuxHost class and its attributes."""

import logging
import socket
import testinfra
from helpers.exec_decorator import exec_command_decorator
from paramiko import AuthenticationException
from typing import Optional


class HostNetworkInterface:
    """Class provides an interface for obtaining information about the network interfaces of the remote host."""

    def __init__(self, name: str, host: testinfra.host.Host):
        """
        :param name: network interface name of the remote server.
        :param host: remote server that owns this network interface.
        """

        self.name = name
        self.interface = host.interface(name)

    def is_interface_exists(self) -> bool:
        """Method returns True if a network interface exists"""

        return self.interface.exists

    def get_speed(self) -> int:
        """Method returns internet connection speed. Example: 1000"""

        return self.interface.speed

    def get_addresses(self) -> list:
        """
        Method returns a list with ip address and mac address of the network interface.
        Example: ['10.0.2.15', 'fe80::523e:df07:463f:7d24']
        """

        return self.interface.addresses


class LinuxHost:
    """The class provides an interface for obtaining information about a linux server."""

    def __init__(self, username, ip_address, path_to_ssh_key):
        """
        :param username: Username for connection to the server.
        :param ip_address: Ip address of the remote server.
        :param path_to_ssh_key: Path to file with private ssh key.
        """

        self.backend = f'paramiko://{username}@{ip_address}'
        self.host = testinfra.get_host(self.backend, ssh_identity_file=path_to_ssh_key)
        self.host_is_available = self.__check_host_availability()
        self.network_interfaces = [HostNetworkInterface(interface, self.host)
                                   for interface in self.get_network_interfaces()
                                   if HostNetworkInterface(interface, self.host).is_interface_exists()]

    def __check_host_availability(self) -> bool:
        """Method returns True if remote server is available."""

        try:
            self.host.run("uptime").stdout
        except Exception as error:
            assert False, f'Linux host is not available! Please, check your input data and host state. {error}'
        return True

    @exec_command_decorator
    def get_cpu_cores_number(self) -> int:
        """Method returns CPU cores number of the linux server. Example: 1"""

        return int(self.host.run("nproc").stdout)

    @exec_command_decorator
    def get_ram_size(self) -> int:
        """Method returns RAM size (Mb) of the linux server. Example: 938"""

        return int(self.host.run("free -m | grep Mem | awk '{print $2}'").stdout)

    @exec_command_decorator
    def get_network_interfaces(self) -> list:
        """Method returns a list with names of network interfaces of the server. Example: ['enp0s3', 'lo']"""

        return self.host.run('ls -A /sys/class/net').stdout.split()

    @exec_command_decorator
    def get_partition_size(self, mount_point: str = '/') -> Optional[int]:
        """Method takes a mount point and returns partition size (Gb) of the linux server. Example: 938"""

        if self.host.mount_point(mount_point).exists:
            return int(self.host.run("lsblk | grep 'part {}' | awk '{}'"
                                     .format(mount_point, '{print $4}')).stdout.replace('G', ''))
        return None

    def is_service_running(self, service: str) -> bool:
        """Method returns True if service is running"""

        return self.host.service(service).is_running

    def is_service_enable(self, service: str) -> bool:
        """Method returns True if service is enabled"""

        return self.host.service(service).is_enabled
