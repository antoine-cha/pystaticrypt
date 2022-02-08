#!/usr/bin/env python
"""Tests for `pystaticrypt` package."""

import pytest
from click.testing import CliRunner

from pystaticrypt import cli
from pystaticrypt.pystaticrypt import decrypt, encrypt


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_hmac():
    password = "test-passphrase"
    contents = "my content"

    encrypted = encrypt(contents, password)
    decrypted = decrypt(encrypted, password)
    assert contents == decrypted


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'pystaticrypt' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
