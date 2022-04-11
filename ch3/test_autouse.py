"""Demonstrate autouse fixtures."""

import pytest
import time


@pytest.fixture(autouse=True, scope="session")
def footer_session_scope():
    """Report the time of the end of session."""
    yield
    now = time.time()
    print("--")
    print("finished : {}".format(time.strftime("%d %b %X", time.localtime(now))))
    print("-----------------")


@pytest.fixture(autouse=True, scope="function")
def footer_function_scope():
    """Report test duration after each function."""
    start = time.time()
    yield
    stop = time.time()
    delta = start - stop
    print("\ntest duration : {:0.3} seconds.".format(delta))


def test_1():
    """Simulate long-ish running test."""
    time.sleep(1)


def test_2():
    """Simulate slightly longer test."""
    time.sleep(1.23)
