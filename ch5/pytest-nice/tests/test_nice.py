"""Testing the pytest-nice plugin."""

import pytest


def test_pass_fail(testdir):

    # create a temporary pytest test module
    testdir.makepyfile("""
        def test_pass():
            assert 1 == 1
        
        def test_fail():
            assert 1 == 2
    """)

    # run pytest
    result = testdir.runpytest()

    # fnmatch_lines does an assertion internally​”
    result.stdout.fnmatch_lines(['*.F*',])  # . for Pass, F for Fail

    # make shure that we get a '1' exit code for the testsuit
    assert result.ret == 1


@pytest.fixture()
def sample_test(testdir):
    testdir.makepyfile("""
        def test_pass():
            assert 1 == 1
        
        def test_fail():
            assert 1 == 2
    """)
    return testdir


def test_with_nice(sample_test):
    result = sample_test.runpytest('--nice')
    result.stdout.fnmatch_lines(['*.O*',])  # . for Pass, O for Fail
    assert result.ret == 1


def test_with_verbose_nice(sample_test):
    result = sample_test.runpytest('-v', '--nice')
    result.stdout.fnmatch_lines(['*::test_fail OPPORTUNITY for improvement*',])
    assert result.ret == 1


def test_non_nice_verbose(sample_test):
    result = sample_test.runpytest('-v')
    result.stdout.fnmatch_lines(['*::test_fail FAILED*']) 
    assert result.ret == 1


def test_header_with_nice(sample_test):
    result = sample_test.runpytest('--nice')
    result.stdout.fnmatch_lines(['You are breathtaking! Thank you  for running tests.'])


def test_header_not_nice(sample_test):   
    result = sample_test.runpytest()
    thanks_message = 'You are breathtaking! Thank you  for running tests.'    
    assert thanks_message not in result.stdout.str()


def test_help_message(testdir):
    result = testdir.runpytest('--help')

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        'nice:',
        '*--nice*nice: turn FAILED into OPPORTUNITY for improvement',
    ])



