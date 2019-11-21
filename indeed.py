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


def extract_indeed_job(job_card):
    title = job_card.find("div", {"class": "title"}).find("a")["title"]

    company = job_card.find("span", {"class": "company"})
    company_anchor = company.find("a")
    if company_anchor is not None:
        company = str(company_anchor.string)
    else:
        company = str(company.string)
    company = company.strip()  # for removing empty space

    location = job_card.find("span", {"class": "location"}).string
    return {"title": title, "company": company, "location": location}


def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        job_cards = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        for job_card in job_cards:
            job = extract_indeed_job(job_card)
            jobs.append(job)
    return jobs
