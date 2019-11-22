import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.co.uk/jobs?q=python&limit={LIMIT}"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})
    links = pagination.find_all("a")
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))
    last_page = pages[-1]
    return last_page


def get_job(job_card):
    title = job_card.find("div", {"class": "title"}).find("a")["title"]
    company = job_card.find("span", {"class": "company"})
    company_anchor = company.find("a")
    if company_anchor is not None:
        company = str(company_anchor.string)
    else:
        company = str(company.string)
    company = company.strip()  # for removing empty space
    location = job_card.find("span", {"class": "location"}).string
    job_id = job_card["data-jk"]
    return {
        "title": title,
        "company": company,
        "location": location,
        "link": f"{URL}&vjk={job_id}",
    }


def get_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping for indeed page: {page + 1}")
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        job_cards = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        for job_card in job_cards:
            job = get_job(job_card)
            jobs.append(job)
    return jobs


def get_indeed_jobs():
    last_page = get_last_page()
    jobs = get_jobs(last_page)
    return jobs

