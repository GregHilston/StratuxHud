"""
Module to help with mocking/bypassing
RaspberryPi specific code to enable for
debugging on a Mac or Windows host.
"""

from sys import platform, version_info

REQUIRED_PYTHON_VERSION = 3.5


def validate_python_version():
    """
    Checks to make sure that the correct version of Python is being used.

    Raises:
        Exception -- If the  version of Python is not new enough.
    """

    python_version = float('{}.{}'.format(
        version_info.major, version_info.minor))
    error_text = 'Requires Python {}'.format(REQUIRED_PYTHON_VERSION)

    if python_version < REQUIRED_PYTHON_VERSION:
        print(error_text)
        raise Exception(error_text)


def is_debug():
    """
    returns True if this should be run as a local debug (Mac or Windows).
    """

    return platform in ["win32", "darwin"]


validate_python_version()
