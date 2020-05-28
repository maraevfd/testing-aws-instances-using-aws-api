import json
import os


def read_expected_data():
    with open(os.path.join('helpers', 'expected.json')) as file:
        expected_data = json.load(file)
    return expected_data
