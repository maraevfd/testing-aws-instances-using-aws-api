"""Module contains a function to read expected data from json file."""

import json
import logging


def read_expected_data(path_to_json: str) -> dict:
    """The function reads the json file and returns its content."""

    try:
        with open(path_to_json) as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error(f'Received invalid file path! Check that the file is spelled correctly {path_to_json}')
