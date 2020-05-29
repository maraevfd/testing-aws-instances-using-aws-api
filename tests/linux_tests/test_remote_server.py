"""Module contains tests for testing linux server."""

import logging
import pytest


def test_cores_number(host, expected_data):
    logging.info(f'Actual cores number: {host.get_cpu_cores_number()},'
                 f' expected cores number: {expected_data["cpu_cores_number"]}')
    assert host.get_cpu_cores_number() == expected_data['cpu_cores_number'], "Incorrect number of processor cores"


def test_network_interfaces_number(host, expected_data):
    logging.info(f'Actual network interfaces number: {len(host.get_network_interfaces())},'
                 f' expected network interfaces number: {expected_data["net_interfaces_number"]}')
    assert len(host.get_network_interfaces()) == expected_data['net_interfaces_number'], "Incorrect number of network "\
                                                                                         "interfaces! "


@pytest.mark.xfail
def test_ram_size(host, expected_data):
    logging.info(f'Actual RAM size: {host.get_ram_size()}Mb, expected RAM size: {expected_data["ram_size"]}Mb')
    assert host.get_ram_size() >= expected_data['ram_size'], "RAM size does not match!"


@pytest.mark.xfail
def test_partition_size(host, expected_data):
    logging.info(f'Actual partition size: {host.get_partition_size()}Gb,'
                 f' expected partition size: {expected_data["partition_size"]}Gb')
    assert host.get_partition_size() >= expected_data['partition_size'], "Partition size does not match!"


def test_is_chronyd_running(host, expected_data):
    logging.info(f'Actual result: chronyd is running -> {host.is_chronyd_running()}'
                 f'expected result: chronyd is running -> {expected_data["is_chronyd_running"]}')
    assert host.is_chronyd_running() == expected_data['is_chronyd_running'], "Chronyd is down!"


def test_is_chronyd_enable(host, expected_data):
    logging.info(f'Actual result: chronyd is enabled -> {host.is_chronyd_enable()}'
                 f'expected result: chronyd is enabled -> {expected_data["is_chronyd_enable"]}')
    assert host.is_chronyd_enable() == expected_data['is_chronyd_enable'], "Chronyd is not enabled!"
