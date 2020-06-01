"""Module contains a decorator for LinuxHost class methods."""

import logging


def exec_command_decorator(command):
    """The function receives a command to run it on a remote server."""

    def wrapper(host_object):
        try:
            return command(host_object)
        except (TypeError, ValueError):
            logging.error('Error executing command on remote server, None returned!')
            return None

    return wrapper
