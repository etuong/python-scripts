# Script to scrape a website to get the number of unique HTML elements

from bs4 import BeautifulSoup
import requests
import sys

hrefs = ["/"]
elements = set()


def scrape(url):
    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text

    # Parse the html content using any parser
    s = BeautifulSoup(html_content, "html.parser")

    for i in s.find_all("a"):
        if ('href' in i.attrs):
            href = i.attrs['href']
            if not href.startswith(("https", "http", "www")) and href not in hrefs:
                href = "/" + href if not href.startswith("/") else href
                hrefs.append(href)
                url = url + href
                print(url)
                scrape(url)

    # Add distinctive HTML elements
    elements.update([tag.name for tag in s.find_all()])


if __name__ == "__main__":
    site = sys.argv[1]
    scrape(site)

    # Display number of unique HTML elements
    print(f'Number of Unique HTML Elements is {len(elements)}')
