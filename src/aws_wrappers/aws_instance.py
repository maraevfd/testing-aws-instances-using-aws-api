"""The module contains the AWSInstance class and its attributes."""

import logging
from src.aws_wrappers.aws_resource import AWSResource
from src.aws_wrappers.ebs_volume import EBSVolume
from src.aws_wrappers.network_interface import NetworkInterface
from typing import Optional


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
    def tags(self) -> Optional[dict]:
        """Attribute returns instance tags. Example: {'Tenant': 'tools', 'Name': 'report_portal'}"""

        try:
            return {tag['Key']: tag['Value'] for tag in self.__instance.tags}
        except KeyError:
            logging.error('Invalid instance tag data received, check it!')
            return None

    @property
    def image_id(self) -> str:
        """Attribute returns instance image id. Example: ami-0062c497b55437b01"""

        return self.__instance.image_id

    @property
    def key_name(self) -> str:
        """Attribute returns instance key name. Example: jenkins_access"""

        return self.__instance.key_name

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
    def state(self) -> Optional[str]:
        """Attribute returns the status of the instance. Example: running"""

        try:
            return self.__instance.state['Name']
        except KeyError:
            logging.error('Unable to retrieve AWSInstance state!')
            return None

    @property
    def security_groups(self) -> Optional[dict]:
        """
        Attribute allows you to see security groups of the instance.
        Example: {'whitelist-lgi': 'sg-0d516428f11e91e89', 'whitelist-connectra': 'sg-009081d7bccf48932'}
        """
        try:
            return {group['GroupName']: group['GroupId'] for group in self.__instance.security_groups}
        except KeyError:
            logging.error('KeyError in AWSInstance security groups! Check it.')
            return None

    @property
    def root_device_type(self) -> str:
        """Attribute returns the type of the root device. Example: ebs"""

        return self.__instance.root_device_type
