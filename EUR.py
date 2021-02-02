import requests
import url
from bs4 import BeautifulSoup


def EUR():
    full_page = requests.get(url.urlEURrub, headers=url.headers)
    soup = BeautifulSoup(full_page.content, "html.parser")
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    return convert[0].text