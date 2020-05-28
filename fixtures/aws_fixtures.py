from src.aws_wrappers.aws_instance import AWSInstance
import pytest


@pytest.fixture(scope='module')
def ec2_instance():
    ec2_instance = AWSInstance('i-06007db6d3063ca53', 'eu-central-1')
    return ec2_instance


@pytest.fixture(scope='module')
def ebs_volume(ec2_instance):
    ebs_volume = ec2_instance.volumes[0]
    return ebs_volume


@pytest.fixture(scope='module')
def network_interface(ec2_instance):
    network_interface = ec2_instance.network_interfaces[0]
    return network_interface

