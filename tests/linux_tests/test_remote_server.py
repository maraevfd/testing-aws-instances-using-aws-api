"""Module contains tests for testing linux server."""

import pytest


def test_cores_number(host, expected_data):
    assert host.get_cpu_cores_number() == expected_data['cpu_cores_number']


def test_network_interfaces_number(host, expected_data):
    assert len(host.get_network_interfaces()) == expected_data['net_interfaces_number']


@pytest.mark.xfail
def test_ram_size(host, expected_data):
    assert host.get_ram_size() >= expected_data['ram_size']


@pytest.mark.xfail
def test_partition_size(host, expected_data):
    assert host.get_partition_size() >= expected_data['partition_size']


def test_is_chronyd_running(host):
    assert host.is_chronyd_running


def test_is_chronyd_enable(host):
    assert host.is_chronyd_enable
