"""
Web scrapping in Python
This is an example of scrapping a web page in Python using beautiful soup

"""

import requests
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup
import time


class WVUScraper:
    """
    A web scraper class for scraping the WVU website.

    Attributes:
    ----------
    base_url : str
        The base URL of the site to scrape (e.g., "https://www.wvu.edu").

    Methods:
    -------
    get_html(url):
        Sends a GET request to the URL and retrieves the HTML content.

    parse_html(html):
        Parses HTML content using BeautifulSoup.

    extract_links(soup):
        Extracts all anchor tags and retrieves link text and URLs.

    extract_headings(soup):
        Extracts all headings (h1, h2, h3) from the parsed HTML content.

    scrape_page(url):
        Scrapes a single page for links and headings.

    follow_links(url, max_pages=5, delay=2):
        Follows links on the page up to a specified number of pages.

    grab_specific_item(soup, selector):
        Extracts specific content based on a CSS selector (e.g., class, id).
    """

    def __init__(self, base_url):
        self.base_url = base_url

    def get_html(self, url):
        """
        Fetches HTML content from a given URL.

        Parameters:
        ----------
        url : str
            The URL to retrieve HTML from.

        Returns:
        -------
        str
            HTML content if the request is successful; None otherwise.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.content
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def parse_html(self, html):
        """
        Parses HTML content using BeautifulSoup.

        Parameters:
        ----------
        html : str
            Raw HTML content to be parsed.

        Returns:
        -------
        BeautifulSoup
            A BeautifulSoup object of the parsed HTML.
        """
        return BeautifulSoup(html, 'html.parser') if html else None

    def extract_links(self, soup):
        """
        Extracts all anchor tags and retrieves link text and URLs.

        Parameters:
        ----------
        soup : BeautifulSoup
            Parsed HTML content.

        Returns:
        -------
        list of dict
            A list of dictionaries containing link text and URLs.
        """
        links = []
        for link in soup.find_all('a', href=True):
            links.append({
                'text': link.text.strip(),
                'url': link.get('href')
            })
        return links

    def extract_headings(self, soup):
        """
        Extracts all headings (h1, h2, h3) from the parsed HTML content.

        Parameters:
        ----------
        soup : BeautifulSoup
            Parsed HTML content.

        Returns:
        -------
        dict
            A dictionary with heading levels as keys and a list of text for each heading as values.
        """
        headings = {}
        for level in ['h1', 'h2', 'h3']:
            headings[level] = [heading.text.strip() for heading in soup.find_all(level)]
        return headings

    def scrape_page(self, url):
        """
        Scrapes a single page for links and headings.

        Parameters:
        ----------
        url : str
            The URL of the page to scrape.

        Returns:
        -------
        dict
            A dictionary containing the page URL, extracted links, and headings.
        """
        html = self.get_html(url)
        if not html:
            return None

        soup = self.parse_html(html)
        data = {
            'url': url,
            'links': self.extract_links(soup),
            'headings': self.extract_headings(soup),
        }
        return data

    def follow_links(self, url, max_pages=5, delay=2):
        """
        Follows links on the main page and scrapes each one up to a specified number of pages.

        Parameters:
        ----------
        url : str
            The initial URL to start scraping from.

        max_pages : int, optional
            The maximum number of pages to scrape (default is 5).

        delay : int, optional
            Delay in seconds between requests to avoid server overload (default is 2).

        Returns:
        -------
        list of dict
            A list of dictionaries, each containing scraped data from a page.
        """
        main_data = self.scrape_page(url)
        if not main_data:
            return []

        all_data = [main_data]
        visited_urls = {url}

        for link in main_data['links']:
            full_url = link['url'] if link['url'].startswith('http') else f"{self.base_url}{link['url']}"
            if full_url not in visited_urls and len(all_data) < max_pages:
                print(f"Scraping {full_url}")
                page_data = self.scrape_page(full_url)
                if page_data:
                    all_data.append(page_data)
                    visited_urls.add(full_url)
                time.sleep(delay)
        return all_data

    def grab_specific_item(self, soup, selector):
        """
        Extracts specific content based on a CSS selector.

        Parameters:
        ----------
        soup : BeautifulSoup
            Parsed HTML content.

        selector : str
            The CSS selector for the item to grab (e.g., '.class' or '#id').

        Returns:
        -------
        list
            A list of strings of content matching the selector.
        """
        items = soup.select(selector)
        return [item.get_text(strip=True) for item in items]


