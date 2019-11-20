import requests
from bs4 import BeautifulSoup

indeed_requests = requests.get("https://www.indeed.co.uk/jobs?q=python&limit=50")

indeed_soup = BeautifulSoup(indeed_requests.text, "html.parser")

pagination = indeed_soup.find("div", {"class": "pagination"})

pages = pagination.find_all("a")

spans = []
for page in pages:
    spans.append(page.find("span"))

print(spans[:-1])  # -1 is first things in reverse

