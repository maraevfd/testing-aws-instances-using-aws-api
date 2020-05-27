"""The module contains the NetworkInterface class and its attributes."""

from src.aws_wrappers.aws_resource import AWSResource


class NetworkInterface(AWSResource):
    """The class provides an interface for obtaining information about the indicated volume."""

    def __init__(self, network_interface_id: str, region_name: str):
        """
        :param network_interface_id: String object to access the network interface.
        :param region_name: A string object that points to the region of the network interface.
        """

        super(NetworkInterface, self).__init__(region_name)
        self.network_interface_id = network_interface_id
        self.__network_interface = self.resource.NetworkInterface(
            network_interface_id)

    @property
    def tags(self) -> list:
        """
        Method returns network interface tags.
        Example: [{'Key': 'Tenant', 'Value': 'tools'}, {'Key': 'Name', 'Value': 'report_portal'}]
        """

        return self.__network_interface.tag_set

    @property
    def tenant(self) -> str:
        """Attribute returns tenant value for given network interface. Example: tools"""

        for tag in self.__network_interface.vpc.tags:
            if tag['Key'] == 'Tenant':
                return tag['Value']
        return 'None'

    @property
    def ip_address(self) -> str:
        """Attribute returns private IPv4 address associated with the network interface. Example: 100.96.255.103"""

        return self.__network_interface.private_ip_address

    @property
    def dns_name(self) -> str:
        """Attribute returns a private dns name. Example: ip-100-96-255-103.eu-central-1.compute.internal"""

        return self.__network_interface.private_dns_name

    @property
    def status(self) -> str:
        """Attribute returns the status of the network interface. Example: in-use"""

        return self.__network_interface.status

    @property
    def vpc_id(self) -> str:
        """Attribute returns vpc id of the network interface. Example: vpc-05569a6be97c3cfd3"""

        return self.__network_interface.vpc_id

    @property
    def total_information(self) -> str:
        """Attribute returns information about the network interface."""

        return f'Total information about network interface ' \
               f'{self.network_interface_id}:\n' \
               f'tags: {self.tags}\n' \
               f'tenant: {self.tenant}\n' \
               f'private ip address: {self.ip_address}\n' \
               f'dns name: {self.dns_name}\n' \
               f'status: {self.status}\n' \
               f'vpc id: {self.vpc_id}'
