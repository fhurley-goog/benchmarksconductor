import os
import pytest
import pandas as pd
from generate_html import generate_html

@pytest.fixture
def cleanup_file():
    """Fixture to clean up the created file after the test."""
    yield
    if os.path.exists("index.html"):
        os.remove("index.html")

def test_generate_html_creates_file(cleanup_file):
    """Tests if the generate_html function creates the index.html file."""
    generate_html("test_data.csv")
    assert os.path.exists("index.html")

def test_generate_html_has_correct_content(cleanup_file):
    """Tests if the generated index.html file has the correct content."""
    generate_html("test_data.csv")
    with open("index.html", "r") as f:
        content = f.read()
    
    # Check for table headers
    assert "<th>Benchmark</th>" in content
    assert "<th>Gemini</th>" in content
    assert "<th>Model A</th>" in content
    assert "<th>Model B</th>" in content

    # Check for table data
    assert "<td>SWE-Bench</td>" in content
    assert "<td>85.2</td>" in content
    assert "<td>83.1</td>" in content
    assert "<td>80.5</td>" in content
    assert "<td>MBPP</td>" in content
    assert "<td>75.4</td>" in content
    assert "<td>72.3</td>" in content
    assert "<td>70.1</td>" in content
