import pytest

@pytest.fixture(scope="session")
def setup():
    print("\n--- API Test Execution Started ---")
    yield
    print("\n--- API Test Execution Completed ---")