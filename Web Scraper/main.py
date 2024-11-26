## Made by Gekko

import requests
from bs4 import BeautifulSoup

# Function to scrape data from a URL
def scrape_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

# Function to process and store the scraped data
def process_data(soup, output_file):
    if soup:
        with open(output_file, 'w', encoding='utf-8') as file:
            # Example: Extract all paragraph texts
            paragraphs = soup.find_all('p')
            for paragraph in paragraphs:
                file.write(paragraph.get_text() + '\n')
        print(f"Data saved to {output_file}")
    else:
        print("No data to process")

def main():
    url = 'https://www.github.com'  # Replace with the URL you want to scrape
    output_file = 'Web Scraper/scraped_data.txt'
    
    soup = scrape_data(url)
    process_data(soup, output_file)

if __name__ == "__main__":
    main()