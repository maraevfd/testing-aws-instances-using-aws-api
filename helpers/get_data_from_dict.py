"""Module contains function to get data from dictionary"""

import logging
from typing import Optional


def get_receive_data(data: dict, key: str, error_message: str) -> Optional[str]:
    """Function requests certain data and logs if it did not find them"""

    if data.get(key):
        return data.get(key)
    logging.error(error_message)
    return None
