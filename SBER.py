import requests
import url
from bs4 import BeautifulSoup


def SBER():
    full_page = requests.get(url.urlSBERrub, headers=url.headers)
    soup = BeautifulSoup(full_page.content, "html.parser")
    convert = soup.findAll("span", {"class": "IsqQVc", "class": "NprOob", "class": "XcVN5d"})
    return convert[0].text