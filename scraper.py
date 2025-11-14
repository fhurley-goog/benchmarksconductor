import requests
from bs4 import BeautifulSoup

def scrape_data(urls):
    """
    Scrapes benchmark data from a list of URLs.

    Args:
        urls (list): A list of URLs to scrape.

    Returns:
        dict: A dictionary containing the scraped benchmark data.
    """
    all_data = {}
    
    # Scraper for the first URL (table-based)
    if len(urls) > 0:
        try:
            response1 = requests.get(urls[0])
            if response1.status_code == 200:
                soup1 = BeautifulSoup(response1.text, 'html.parser')
                table = soup1.find('table')
                if table:
                    rows = table.find_all('tr')
                    if len(rows) > 1:
                        headers = [header.text.strip() for header in rows[0].find_all('th')]
                        for row in rows[1:]:
                            cols = row.find_all('td')
                            benchmark_name = cols[0].text.strip()
                            all_data[benchmark_name] = {}
                            for i, col in enumerate(cols[1:], 1):
                                model_name = headers[i]
                                all_data[benchmark_name][model_name] = col.text.strip()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {urls[0]}: {e}")

    # Scraper for the second URL (div-based)
    if len(urls) > 1:
        try:
            response2 = requests.get(urls[1])
            if response2.status_code == 200:
                soup2 = BeautifulSoup(response2.text, 'html.parser')
                data_div = soup2.find('div', id='benchmark-data')
                if data_div:
                    benchmark_name = data_div.find('h2').text.strip()
                    all_data[benchmark_name] = {}
                    paragraphs = data_div.find_all('p')
                    for p in paragraphs:
                        parts = p.text.split(':')
                        model_name = parts[0].strip()
                        score = parts[1].strip()
                        all_data[benchmark_name][model_name] = score
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {urls[1]}: {e}")

    return all_data

if __name__ == "__main__":
    # Example usage:
    # Note: These URLs are placeholders for the actual benchmark sites.
    urls_to_scrape = [
        "http://benchmark-site-1.com",
        "http://benchmark-site-2.com"
    ]
    scraped_data = scrape_data(urls_to_scrape)
    print(scraped_data)
