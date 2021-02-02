import requests
import url
from bs4 import BeautifulSoup


def bit_rub():
    full_page = requests.get(url.urlBITrub, headers=url.headers)
    soup = BeautifulSoup(full_page.content, "html.parser")
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    return convert[0].text

def bit_usd():
    full_page = requests.get(url.urlBITusd, headers=url.headers)
    soup = BeautifulSoup(full_page.content, "html.parser")
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    return convert[0].text


