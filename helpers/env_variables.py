"""The module contains global variables and a function to extract them."""

import logging
import os
from typing import Optional

EXPECTED_DATA_FILE = 'expected_data.json'


def get_env_variable(var_name: str) -> Optional[str]:
    """The function gets the variable from the global environment."""

    if os.environ.get(var_name):
        return os.environ.get(var_name)
    logging.error(f'{var_name} variable was not found!')
    return None
