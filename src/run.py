"""This module is designed to obtain information about the instance."""

from src.aws_wrappers.aws_instance import AWSInstance
import os

if __name__ == '__main__':
    ec2_instance = AWSInstance(os.environ.get("INSTANCE_ID"), os.environ.get("REGION_NAME"))
    print(ec2_instance.total_information)

    volume = ec2_instance.volumes[0]
    print(volume.total_information)

    network_interface = ec2_instance.network_interfaces[0]
    print(network_interface.total_information)
