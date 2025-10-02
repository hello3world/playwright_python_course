import pytest


def test_initial_check(pre_work, settings):
    print('This is first test')
    assert pre_work == "pass"

@pytest.mark.smoke
def test_second_check(pre_work_2):
    print('This is second test')
    assert pre_work_2 == "fail"

@pytest.mark.skip
def test_third_check(pre_work_2, settings):
    print('This is second test')
    assert pre_work_2 == "pass"