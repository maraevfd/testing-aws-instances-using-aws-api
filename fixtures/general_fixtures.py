"""Module contains general fixtures for testing."""

import logging
import os
import pytest
from helpers.json_reader import read_expected_data
from helpers.env_variables import EXPECTED_DATA_FILE
from typing import Optional


@pytest.fixture(scope='session')
def expected_data(request) -> Optional[dict]:
    """Fixture returns a dictionary that contains the expected data for testing."""

    try:
        return read_expected_data(os.path.join(request.config.invocation_dir, EXPECTED_DATA_FILE))
    except FileNotFoundError as error:
        logging.error('File with expected data not found!', error)
        return None
