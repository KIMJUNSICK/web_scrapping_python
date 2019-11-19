import requests
from bs4 import BeautifulSoup

indeed_requests = requests.get("https://www.indeed.co.uk/jobs?q=python&limit=50")

print(indeed_requests)

indeed_soup = BeautifulSoup(indeed_requests.text, "html.parser")

print(indeed_soup)
