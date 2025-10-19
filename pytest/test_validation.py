import pytest

@pytest.fixture(scope="function")
def pre_work():
    print("keep fighting")
    return "pass"

@pytest.fixture(scope="function")
def second_work():
    print("I setup Second Work")
    yield
    print("Tear down the work")


def test_validation(pre_setup):
    print("Hello Pycharm")

def test_verification(pre_work, second_work):
    print("Hello PyTorch")
    assert pre_work =="pass"