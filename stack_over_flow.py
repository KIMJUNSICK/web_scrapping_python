import requests
from bs4 import BeautifulSoup

URL = "https://stackoverflow.com/jobs?q=python&sort=i"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "pagination"}).find_all("a")
    last_pages = pages[-2].get_text(strip=True)
    return int(last_pages)


def get_stack_over_flow_jobs():
    last_page = get_last_page()
    return last_page


print(get_stack_over_flow_jobs())
