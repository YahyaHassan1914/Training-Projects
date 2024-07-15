import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging

"""
- It does not really work
- Too lasy to fix
"""


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to scrape a single page
def scrape_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        logging.error(f'HTTP Error: {errh}')
        return []
    except requests.exceptions.ConnectionError as errc:
        logging.error(f'Error Connecting: {errc}')
        return []
    except requests.exceptions.Timeout as errt:
        logging.error(f'Timeout Error: {errt}')
        return []
    except requests.exceptions.RequestException as err:
        logging.error(f'Oops: Something Else {err}')
        return []

    soup = BeautifulSoup(response.text, 'lxml')
    articles = soup.find_all('article')
    data = []

    for article in articles:
        title = article.find('h2').text.strip()
        link = article.find('a')['href']
        data.append({'title': title, 'link': link})

    return data

# Function to scrape a site with dynamic content using Selenium
def scrape_dynamic_page(url):
    driver = webdriver.Chrome()  # Or your preferred driver
    driver.get(url)

    # Allow time for JavaScript to load the content
    time.sleep(5)

    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'lxml')
    driver.quit()

    articles = soup.find_all('article')
    data = []

    for article in articles:
        title = article.find('h2').text.strip()
        link = article.find('a')['href']
        data.append({'title': title, 'link': link})

    return data

# Main scraping function with pagination
def scrape_website(base_url, dynamic=False):
    page_number = 1
    all_data = []

    while True:
        url = f'{base_url}{page_number}'
        logging.info(f'Scraping page: {url}')

        if dynamic:
            page_data = scrape_dynamic_page(url)
        else:
            page_data = scrape_page(url)

        if not page_data:
            logging.info('No more data found. Ending scraping.')
            break

        all_data.extend(page_data)
        page_number += 1
        time.sleep(2)  # Politeness delay

    return all_data

# Save data to CSV
def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    logging.info(f'Data saved to {filename}')

# Main function to prompt user for input and start scraping
def main():
    base_url = input("Enter the base URL of the website (e.g., 'https://example.com/page/'): ")
    dynamic_content = input("Is the content dynamically loaded with JavaScript? (yes/no): ").strip().lower() == 'yes'
    
    data = scrape_website(base_url, dynamic=dynamic_content)
    if data:
        filename = input("Enter the filename to save the data (e.g., 'scraped_data.csv'): ")
        save_to_csv(data, filename)
    else:
        logging.info('No data scraped.')

if __name__ == '__main__':
    main()