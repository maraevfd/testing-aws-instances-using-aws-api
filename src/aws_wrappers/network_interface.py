"""The module contains the NetworkInterface class and its methods."""

from src.aws_wrappers.aws_resource import AWSResource


class NetworkInterface(AWSResource):
    """
    The class provides an interface for obtaining information about
    the indicated volume.
    """

    def __init__(self, network_interface_id, region_name):
        """
        Constructor.

        :param network_interface_id: String object to access the network
        interface.
        :param region_name: A string object that points to the region
        of the network interface.
        """
        super(NetworkInterface, self).__init__(region_name)
        self.network_interface_id = network_interface_id
        self.__network_interface = self.resource.NetworkInterface(
            network_interface_id)

    @property
    def get_tags(self):
        """Method returns network interface tags."""

        return self.__network_interface.tag_set

    @property
    def get_tenant(self):
        """Method returns a vpc object."""

        return self.__network_interface.vpc

    @property
    def get_ip_address(self):
        """The private IPv4 address associated with the network interface."""

        return self.__network_interface.private_ip_address

    @property
    def get_dns_name(self):
        """Method returns a private dns name."""

        return self.__network_interface.private_dns_name

    @property
    def get_status(self):
        """Method returns the status of the network interface."""

        return self.__network_interface.status

    @property
    def get_vpc_id(self):
        """Method returns vpc id of the network interface."""

        return self.__network_interface.vpc_id

    @property
    def get_total_information(self):
        """The method returns information about the network interface."""

        return f'Total information about network interface ' \
               f'{self.network_interface_id}:\n' \
               f'tags: {self.get_tags}\n' \
               f'tenant: {self.get_tenant()}\n' \
               f'private ip address: {self.get_ip_address}\n' \
               f'dns name: {self.get_dns_name}\n' \
               f'status: {self.get_status}\n' \
               f'vpc id: {self.get_vpc_id}'
