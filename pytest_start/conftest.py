import pytest

@pytest.fixture(scope="session")
def pre_work():
    print('\npreSetup')
    return "pass"

@pytest.fixture(scope="function")
def pre_work_2():
    print('\npreSetup')
    return "fail"

@pytest.fixture(scope="function")
def settings():
    print('\nset up settings')
    yield
    print('\ndear down settings')