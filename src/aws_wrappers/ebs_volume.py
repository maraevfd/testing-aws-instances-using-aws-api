"""The module contains the EBSVolume class and its attributes."""

from src.aws_wrappers.aws_resource import AWSResource


class EBSVolume(AWSResource):
    """
    The class provides an interface for obtaining information about
    the indicated volume.
    """

    def __init__(self, volume_id: str, region_name: str):
        """
        :param volume_id: String object to access the volume.
        :param region_name: A string object that points to the region of the volume.
        """

        super(EBSVolume, self).__init__(region_name)
        self.volume_id = volume_id
        self.__volume = self.resource.Volume(volume_id)

    @property
    def tags(self) -> list:
        """
        Attribute returns volume tags.
        Example: [{'Key': 'Tenant', 'Value': 'tools'}, {'Key': 'Name', 'Value': 'report_portal'}]
        """

        return self.__volume.tags

    @property
    def size(self) -> int:
        """Attribute returns the size of the volume in gigabytes. Example: 50"""

        return self.__volume.size

    @property
    def type(self) -> str:
        """Attribute returns volume type. Example: gp2"""

        return self.__volume.volume_type

    @property
    def state(self) -> str:
        """Attribute returns the status of the volume at the moment. Example: in-use"""

        return self.__volume.state

    @property
    def total_information(self) -> str:
        """Attribute returns necessary information about the volume."""

        return f'Total information about volume {self.volume_id}:\n' \
               f'tags: {self.tags}\n' \
               f'size: {self.size}Gb\n' \
               f'type: {self.type}\n' \
               f'state: {self.state}'
