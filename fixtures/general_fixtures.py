"""Module contains general fixtures for testing."""

import logging
import os
import pytest
from helpers.json_reader import read_expected_data
from helpers.env_variables import EXPECTED_DATA_FILE


@pytest.fixture(scope='session')
def expected_data(request) -> dict:
    """Fixture returns a dictionary that contains the expected data for testing."""

    try:
        return read_expected_data(os.path.join(request.config.invocation_dir, EXPECTED_DATA_FILE))
    except FileNotFoundError:
        logging.error('File with expected data not found!')
