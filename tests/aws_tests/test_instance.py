"""Module contains tests for testing aws instance."""

import logging


def test_instance_state(ec2_instance, expected_ec2_state):
    logging.info(f'Actual state: {ec2_instance.state}, expected state: {expected_ec2_state}')
    assert ec2_instance.state == expected_ec2_state, "Error in 'state' assertion!"


def test_instance_type(ec2_instance, expected_ec2_type):
    logging.info(f'Actual instance type: {ec2_instance.type}, expected instance type: {expected_ec2_type}')
    assert ec2_instance.type == expected_ec2_type, "Error in 'type' assertion!"


def test_network_interface_number(ec2_network_interface_number, expected_net_interface_num):
    logging.info(f'Actual network interfaces number: {ec2_network_interface_number}, '
                 f'expected network interfaces number: {expected_net_interface_num}')
    assert ec2_network_interface_number == expected_net_interface_num, "Incorrect number of the network interfaces! "


def test_instance_tags_count(ec2_tags_number, expected_tags_number):
    logging.info(f'Actual tags number: {ec2_tags_number}, expected tags number: {expected_tags_number}')
    assert ec2_tags_number == expected_tags_number, 'Incorrect number of the instance tags!'


def test_instance_tag_name(ec2_tag_name_value, expected_tag_name):
    logging.info(f'Actual name tag: {ec2_tag_name_value}, expected name tag: {expected_tag_name}')
    assert ec2_tag_name_value == expected_tag_name, 'Invalid name tag value!'


def test_instance_key_name(ec2_instance, expected_ec2_key_name):
    logging.info(f'Actual key name: {ec2_instance.key_name}, expected key name: {expected_ec2_key_name}')
    assert ec2_instance.key_name == expected_ec2_key_name, 'Invalid ssh key name!'


def test_root_device_type(ec2_instance, expected_root_device):
    logging.info(f'Actual root device type: {ec2_instance.root_device_type}, '
                 f'expected root device type: {expected_root_device}')
    assert ec2_instance.root_device_type == expected_root_device, 'Invalid root device type!'


def test_ebs_size(ec2_instance, expected_volume_size):
    for volume in ec2_instance.get_volumes():
        logging.info(f'Actual EBS volume size: {volume.size}, expected EBS volume size:{expected_volume_size}')
        assert volume.size >= expected_volume_size, 'Invalid volume size!'


def test_network_interface_private_ip(ec2_instance, expected_private_ip):
    logging.info(f'Actual private ip: {ec2_instance.private_ip}, expected private ip: {expected_private_ip}')
    assert ec2_instance.private_ip == expected_private_ip, 'Invalid private ip address!'


def test_network_interface_public_ip(ec2_instance, expected_public_ip):
    logging.info(f'Actual public ip: {ec2_instance.public_ip}, expected public ip: {expected_public_ip}')
    assert ec2_instance.public_ip == expected_public_ip, 'Invalid public ip address!'
