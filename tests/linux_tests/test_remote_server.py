"""Module contains tests for testing linux server."""

import logging


def test_cores_number(cpu_number, expected_cpu_number):
    logging.info(f'Actual cores number: {cpu_number}, '
                 f'expected cores number: {expected_cpu_number}')
    assert cpu_number >= expected_cpu_number, "Incorrect number of processor cores"


def test_network_interfaces_number(network_interfaces_number, expected_network_interfaces_number):
    logging.info(f'Actual network interfaces number: {network_interfaces_number}, '
                 f'expected network interfaces number: {expected_network_interfaces_number}')
    assert network_interfaces_number == expected_network_interfaces_number, "Incorrect number of network " \
                                                                            "interfaces!"


def test_ram_size(ram_size, expected_ram_size):
    logging.info(f'Actual RAM size: {ram_size}Mb, expected RAM size: {expected_ram_size}Mb')
    assert ram_size >= expected_ram_size, "RAM size does not match!"


def test_partition_size(partition_size, expected_partition_size):
    logging.info(f'Actual partition size: {partition_size}Gb, '
                 f'expected partition size: {expected_partition_size}Gb, ')
    assert partition_size >= expected_partition_size, "Partition size does not match!"


def test_is_chronyd_running(chronyd_is_running, expected_chronyd_is_running):
    logging.info(f'Actual result: chronyd is running -> {chronyd_is_running}, '
                 f'expected result: chronyd is running -> {expected_chronyd_is_running}')
    assert chronyd_is_running == expected_chronyd_is_running, "Chronyd is down!"


def test_is_chronyd_enable(chronyd_is_enable, expected_chronyd_is_enable):
    logging.info(f'Actual result: chronyd is enabled -> {chronyd_is_enable}, '
                 f'expected result: chronyd is enabled -> {expected_chronyd_is_enable}')
    assert chronyd_is_enable == expected_chronyd_is_enable, "Chronyd is not enabled!"
