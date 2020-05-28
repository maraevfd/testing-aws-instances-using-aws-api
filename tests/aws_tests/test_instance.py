import json
import os

with open(os.path.join('helpers', 'expected.json')) as file:
    expected_data = json.load(file)


def test_instance_state(ec2_instance):
    assert ec2_instance.state == expected_data['state']


def test_instance_type(ec2_instance):
    assert ec2_instance.type == expected_data['type']


def test_network_interface_number(ec2_instance):
    assert len(ec2_instance.network_interfaces) == expected_data['net_interfaces_number']


def test_instance_tags_count(ec2_instance):
    assert len(ec2_instance.tags) == expected_data['tags_number']


def test_instance_tag_name(ec2_instance):
    assert ec2_instance.tags['Name'] == expected_data['tag_name']


def test_instance_key_name(ec2_instance):
    assert ec2_instance.key_name == expected_data['ssh_key_name']


def test_root_device_type(ec2_instance):
    assert ec2_instance.root_device_type == expected_data['root_device_type']


def test_volume_size(ebs_volume):
    assert ebs_volume.size == expected_data['ebs_size']


def test_network_interface_private_ip(network_interface):
    assert network_interface.private_ip_address == expected_data['private_ip']


def test_network_interface_public_ip(network_interface):
    assert network_interface.public_ip_address == expected_data['public_ip']
