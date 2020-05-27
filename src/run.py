"""This module is designed to obtain information about the instance."""

from src.aws_wrappers.aws_instance import AWSInstance


if __name__ == '__main__':
    ec2_instance = AWSInstance('i-06007db6d3063ca53', 'eu-central-1')
    print(ec2_instance.get_total_information)

    volume = ec2_instance.volumes[0]
    print(volume.get_total_information)

    network_interface = ec2_instance.network_interfaces[0]
    print(network_interface.get_total_information)
