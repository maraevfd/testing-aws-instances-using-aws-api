"""Module contains a function to read expected data from json file."""

import json


def read_expected_data(path_to_json) -> dict:
    """The function reads the json file and returns its content."""

    with open(path_to_json) as file:
        return json.load(file)
