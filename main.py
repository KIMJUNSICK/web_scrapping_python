import requests
from bs4 import BeautifulSoup

indeed_requests = requests.get("https://www.indeed.co.uk/jobs?q=python&limit=50")

indeed_soup = BeautifulSoup(indeed_requests.text, "html.parser")

pagination = indeed_soup.find("div", {"class": "pagination"})

links = pagination.find_all("a")

pages = []
for link in links[:-1]:
    pages.append(int(link.string))

max_page = pages[-1]
