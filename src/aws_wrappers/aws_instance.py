"""The module contains the AWSInstance class and its methods."""

from src.aws_wrappers.aws_resource import AWSResource
from src.aws_wrappers.ebs_volume import EBSVolume
from src.aws_wrappers.network_interface import NetworkInterface


class AWSInstance(AWSResource):
    """
    The class provides an interface for obtaining information about
    a specific instance.
    """

    def __init__(self, instance_id, region_name):
        """
        Constructor.

        :param instance_id: String object to access the instance.
        :param region_name: A string object that points to the region
        of the instance.
        """

        super(AWSInstance, self).__init__(region_name)
        self.instance_id = instance_id
        self.__instance = self.resource.Instance(instance_id)
        self.volumes = [EBSVolume(volume.id, region_name)
                        for volume in self.__instance.volumes.all()]
        self.network_interfaces = [NetworkInterface(network_interface.id,
                                                    region_name)
                                   for network_interface
                                   in self.__instance.network_interfaces]

    @property
    def tags(self):
        """Method returns instance tags."""

        return self.__instance.tags

    @property
    def image_id(self):
        """Method returns instance image id."""

        return self.__instance.image_id

    @property
    def private_ip(self):
        """Method returns instance private ip address."""

        return self.__instance.private_ip_address

    @property
    def public_ip(self):
        """Method returns instance public ip address."""

        return self.__instance.public_ip_address

    @property
    def state(self):
        """The method returns the status of the instance."""

        return self.__instance.state

    @property
    def security_groups(self):
        """The method allows you to see security groups of the instance."""

        return self.__instance.security_groups

    @property
    def total_information(self):
        """The method returns necessary information about the instance."""

        return f'Total information:\ntags: {self.tags}\n' \
               f'private ip address: {self.private_ip}\n' \
               f'image id: {self.image_id}\n' \
               f'public ip address: {self.public_ip}\n' \
               f'state: {self.state}\n' \
               f'security groups: {self.security_groups}\n'\
               f'number of volumes: {len(self.volumes)}\n' \
               f'number of network interfaces: {len(self.network_interfaces)}'
