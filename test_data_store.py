import os
import pytest
from data_store import create_data_store

@pytest.fixture
def cleanup_file():
    """Fixture to clean up the created file after the test."""
    yield
    if os.path.exists("data.csv"):
        os.remove("data.csv")

def test_create_data_store_creates_file(cleanup_file):
    """Tests if the create_data_store function creates the data.csv file."""
    create_data_store()
    assert os.path.exists("data.csv")

def test_create_data_store_has_correct_header(cleanup_file):
    """Tests if the created data.csv file has the correct header."""
    create_data_store()
    with open("data.csv", "r") as f:
        header = f.readline().strip()
    assert header == "Benchmark,Gemini,Model A,Model B"
