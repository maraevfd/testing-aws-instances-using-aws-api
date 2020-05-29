"""Module contains a function to read expected data from json file."""

import json
import os


def read_expected_data() -> dict:
    """The function reads the json file and returns its content."""

    with open(os.path.join(os.environ.get("PATH_TO_PROJECT"), 'helpers', 'expected.json')) as file:
        return json.load(file)
