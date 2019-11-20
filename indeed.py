import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.co.uk/jobs?q=python&limit={LIMIT}"


def extract_indeed_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})
    links = pagination.find_all("a")
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))
    last_page = pages[-1]
    return last_page


def extract_indeed_jobs(last_page):
    for page in range(last_page):
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        job_cards = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        for job_card in job_cards:
            title = job_card.find("div", {"class": "title"}).find("a")["title"]
            print(title)
