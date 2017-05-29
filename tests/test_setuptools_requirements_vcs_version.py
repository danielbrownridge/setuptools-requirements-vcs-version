"""
Tests for the setuptools-requirements-vcs-version module.
"""

from setuptools_requirements_vcs_version import get_version

def test_get_version():
    """
    Check that a version can be retrieved from requiremnts data.
    """

    version = get_version()

    print(version)

    assert False
