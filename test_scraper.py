import pytest
import requests
from scraper import scrape_data

@pytest.fixture
def mock_response_1(mocker):
    """Fixture to mock a successful response from a benchmark site."""
    mock = mocker.Mock()
    mock.status_code = 200
    mock.text = """
    <html>
        <body>
            <table>
                <tr>
                    <th>Benchmark</th>
                    <th>Gemini</th>
                    <th>Model A</th>
                </tr>
                <tr>
                    <td>Benchmark 1</td>
                    <td>95.5</td>
                    <td>92.3</td>
                </tr>
            </table>
        </body>
    </html>
    """
    return mock

@pytest.fixture
def mock_response_2(mocker):
    """Fixture to mock a successful response from another benchmark site."""
    mock = mocker.Mock()
    mock.status_code = 200
    mock.text = """
    <html>
        <body>
            <div id="benchmark-data">
                <h2>Benchmark 2</h2>
                <p>Gemini: 88.1</p>
                <p>Model B: 89.5</p>
            </div>
        </body>
    </html>
    """
    return mock

def test_scrape_data_with_two_sources(mocker, mock_response_1, mock_response_2):
    """
    Tests scraping data from two different mock sources and merging the results.
    """
    # Mock the requests.get to return different responses for different URLs
    mocker.patch('requests.get', side_effect=[mock_response_1, mock_response_2])
    
    urls = ["http://benchmark-site-1.com", "http://benchmark-site-2.com"]
    scraped_data = scrape_data(urls)

    expected_data = {
        "Benchmark 1": {"Gemini": "95.5", "Model A": "92.3"},
        "Benchmark 2": {"Gemini": "88.1", "Model B": "89.5"}
    }
    
    assert scraped_data == expected_data
