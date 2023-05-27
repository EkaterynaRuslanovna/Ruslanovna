from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup


def parse_html(url: str, endpoint: str = "", params=None):
    if params is None:
        params = {}
    response = requests.get(url + endpoint, params)
    if response.status_code == 200:
        html_parser = BeautifulSoup(response.text, "html.parser")       # розпарсити HTML
        links = []
        for link in html_parser.find_all('a'):                          # шукає атрибути HTML <a>
            href_attribute = link.get("href")                           # отримуємо вміст(лінки) атрибутів href
            if href_attribute:
                links.append(href_attribute)
        return links


def validate_link(link: str, url: str):
    if link.startswith("/url?q="):
        link = link[7:]
    if link.startswith("/"):
        link = urljoin(url, link)
    return link


def validate_links(links: list, url: str):
    valid_links = []
    invalid_links = []
    for link in links:
        link = validate_link(link, url)
        response = requests.get(link)
        if response.status_code == 200:
            valid_links.append(link)
        else:
            invalid_links.append(link)
    with open("valid_links.txt", "w", encoding="utf-8") as valid_file:
        valid_file.write("\n".join(valid_links))
    with open("broken_links.txt", "w", encoding="utf-8") as invalid_file:
        invalid_file.write("\n".join(invalid_links))
    print("Лінки успішно провалідовані")
