"""
Tests for the setuptools-requirements-vcs-version module.
"""

from setuptools_requirements_vcs_version import get_version

def test_get_version():
    """
    Check that a version can be retrieved from requiremnts data.
    """
    name = "foo"
    requirments = "git+https://example.com/path/repo.git@1.2.3#egg=foo"

    version = get_version(name, requirments)

    assert version == "1.2.3"
