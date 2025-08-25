
import pytest


@pytest.fixture(scope="session")

def pre_setup():
    print("I am setting up the browser")