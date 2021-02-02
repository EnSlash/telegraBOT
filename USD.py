import requests
import url
from bs4 import BeautifulSoup


def USD():
    full_page = requests.get(url.urlUSDrub, headers=url.headers)
    soup = BeautifulSoup(full_page.content, "html.parser")
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    return convert[0].text