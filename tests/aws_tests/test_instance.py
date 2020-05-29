"""Module contains tests for testing aws instance."""

import logging


def test_instance_state(ec2_instance, expected_data):
    logging.info(f'Actual state: {ec2_instance.state}, expected state: {expected_data["state"]}')
    assert ec2_instance.state == expected_data['state'], "Error in 'state' assertion!"


def test_instance_type(ec2_instance, expected_data):
    logging.info(f'Actual instance type: {ec2_instance.type}, expected instance type: {expected_data["type"]}')
    assert ec2_instance.type == expected_data['type'], "Error in 'type' assertion!"


def test_network_interface_number(ec2_instance, expected_data):
    logging.info(f'Actual network interfaces number: {len(ec2_instance.network_interfaces)}, '
                 f'expected network interfaces number: {expected_data["net_interfaces_number"]}')
    assert len(ec2_instance.network_interfaces) == expected_data['net_interfaces_number'], "Incorrect number of " \
                                                                                           "the network interfaces! "


def test_instance_tags_count(ec2_instance, expected_data):
    logging.info(f'Actual tags number: {len(ec2_instance.tags)}, expected tags number: {expected_data["tags_number"]}')
    assert len(ec2_instance.tags) == expected_data['tags_number'], 'Incorrect number of the instance tags!'


def test_instance_tag_name(ec2_instance, expected_data):
    logging.info(f'Actual name tag: {ec2_instance.tags["Name"]}, expected name tag: {expected_data["tag_name"]}')
    assert ec2_instance.tags['Name'] == expected_data['tag_name'], 'Invalid name tag value!'


def test_instance_key_name(ec2_instance, expected_data):
    logging.info(f'Actual key name: {ec2_instance.key_name}, expected key name: {expected_data["ssh_key_name"]}')
    assert ec2_instance.key_name == expected_data['ssh_key_name'], 'Invalid ssh key name!'


def test_root_device_type(ec2_instance, expected_data):
    logging.info(f'Actual root device type: {ec2_instance.root_device_type}, '
                 f'expected root device type: {expected_data["root_device_type"]}')
    assert ec2_instance.root_device_type == expected_data['root_device_type'], 'Invalid root device type!'


def test_ebs_size(ec2_instance, expected_data):
    for volume in ec2_instance.volumes:
        logging.info(f'Actual EBS volume size: {volume.size}, expected EBS volume size:{expected_data["ebs_size"]}')
        assert volume.size >= expected_data['ebs_size'], 'Invalid volume size!'


def test_network_interface_private_ip(ec2_instance, expected_data):
    logging.info(f'Actual private ip: {ec2_instance.private_ip}, expected private ip: {expected_data["private_ip"]}')
    assert ec2_instance.private_ip == expected_data['private_ip'], 'Invalid private ip address!'


def test_network_interface_public_ip(ec2_instance, expected_data):
    logging.info(f'Actual public ip: {ec2_instance.public_ip}, expected public ip: {expected_data["public_ip"]}')
    assert ec2_instance.public_ip == expected_data['public_ip'], 'Invalid public ip address!'
