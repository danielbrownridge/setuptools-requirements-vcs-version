"""
Tests for the setuptools-requirements-vcs-version module.
"""

from subprocess import run

from setuptools_requirements_vcs_version import get_version

def test_get_version():
    """
    Check that a version can be retrieved from requiremnts data.
    """
    name = "foo"
    requirements = "git+https://example.com/path/repo.git@1.2.3#egg=foo"

    version = get_version(name, requirements)

    assert str(version) == "1.2.3"
    assert version.major == 1
    assert version.minor == 2
    assert version.patch == 3

def test_get_version_from_file():
    """
    Check that a version can be retrieved when a requirements.txt file is
    supplied.

    """
    name = "foo"

    version = get_version(name)

    assert str(version) == "1.2.3"
