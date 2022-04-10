"""Demo fixture scope."""

import pytest


@pytest.fixture(scope='function')
def func_scope():
    """A function scope fixture."""


@pytest.fixture(scope='module')
def mod_scope():
    """A module scope fixture."""


@pytest.fixture(scope='session')
def sess_scope():
    """A session scope fixture."""


@pytest.fixture(scope="class")
def class_scope():
    """A class scope fixture."""


def test_1(sess_scope, func_scope, mod_scope):
    """Test using session, module and funciton scope fixtures."""


def test_2(sess_scope, func_scope, mod_scope):
    """Demo is more fun with multiple tests."""


@pytest.mark.usefixtures('class_scope')
class Test_something():
    """Demo class scope fixtures."""

    def test_3(self):
        """Test using a class scope fixture."""

    def test_4(self):
        """Again, multiple tests are more fun."""
