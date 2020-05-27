"""The module contains the AWSResource class."""

import boto3


class AWSResource:
    """Base class for creating the EC2 service"""

    def __init__(self, region_name: str):
        """
        :param region_name: A string object that points to the region of the EC2 instance.
        """

        self.resource = boto3.resource('ec2', region_name=region_name)
        self.client = boto3.client('ec2', region_name=region_name)
