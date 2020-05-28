"""The module contains the AWSInstance class and its attributes."""

from src.aws_wrappers.aws_resource import AWSResource
from src.aws_wrappers.ebs_volume import EBSVolume
from src.aws_wrappers.network_interface import NetworkInterface


class AWSInstance(AWSResource):
    """The class provides an interface for obtaining information about a specific instance."""

    def __init__(self, instance_id: str, region_name: str):
        """
        :param instance_id: String object to access the instance.
        :param region_name: A string object that points to the region of the instance.
        """

        super(AWSInstance, self).__init__(region_name)
        self.instance_id = instance_id
        self.__instance = self.resource.Instance(instance_id)
        self.volumes = [EBSVolume(volume.id, region_name)
                        for volume in self.__instance.volumes.all()]
        self.network_interfaces = [NetworkInterface(network_interface.id, region_name)
                                   for network_interface in self.__instance.network_interfaces]

    @property
    def tags(self) -> dict:
        """Attribute returns instance tags. Example: {'Tenant': 'tools', 'Name': 'report_portal'}"""

        return {tag['Key']: tag['Value'] for tag in self.__instance.tags}

    @property
    def image_id(self) -> str:
        """Attribute returns instance image id. Example: ami-0062c497b55437b01"""

        return self.__instance.image_id

    @property
    def type(self) -> str:
        """Attribute returns instance type. Example: r5.xlarge"""

        return self.__instance.instance_type

    @property
    def private_ip(self) -> str:
        """Attribute returns instance private ip address. Example: 100.96.255.103"""

        return self.__instance.private_ip_address

    @property
    def public_ip(self) -> str:
        """Attribute returns instance public ip address. Example: 18.196.198.93"""

        return self.__instance.public_ip_address

    @property
    def state(self) -> str:
        """Attribute returns the status of the instance. Example: running"""

        return self.__instance.state['Name']

    @property
    def security_groups(self) -> dict:
        """
        Attribute allows you to see security groups of the instance.
        Example: {'whitelist-lgi': 'sg-0d516428f11e91e89', 'whitelist-connectra': 'sg-009081d7bccf48932'}
        """

        return {group['GroupName']: group['GroupId'] for group in self.__instance.security_groups}

    @property
    def total_information(self) -> str:
        """Attribute returns necessary information about the instance."""

        return f'Total information:\ntags: {self.tags}\n' \
               f'private ip address: {self.private_ip}\n' \
               f'image id: {self.image_id}\n' \
               f'public ip address: {self.public_ip}\n' \
               f'state: {self.state}\n' \
               f'security groups: {self.security_groups}\n'\
               f'number of volumes: {len(self.volumes)}\n' \
               f'number of network interfaces: {len(self.network_interfaces)}'
