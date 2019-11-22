import requests
from bs4 import BeautifulSoup

URL = "https://stackoverflow.com/jobs?q=python&sort=i"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "pagination"}).find_all("a")
    last_pages = pages[-2].get_text(strip=True)
    return int(last_pages)


def get_job(job_summary):
    title = job_summary.find("div", {"class": "-title"}).find("a").string
    company, location = job_summary.find("div", {"class": "-company"}).find_all(
        "span", recursive=False
    )  # recursive = False is meant that don't dig deeply, only one layer that we request
    # python syntax like 'company, location =' must be used when you know elements
    company = company.get_text(strip=True)
    location = location.get_text(strip=True).strip("-").strip(" \r").strip("\n")
    job_id = job_summary["data-jobid"]
    return {
        "title": title,
        "company": company,
        "location": location,
        "link": f"https://stackoverflow.com/jobs/{job_id}",
    }


def get_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping for stack0verflow page {page + 1}")
        result = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        job_summarys = soup.find_all("div", {"class": "-job"})
        for job_summary in job_summarys:
            job = get_job(job_summary)
            jobs.append(job)
    return jobs


def get_stack_over_flow_jobs():
    last_page = get_last_page()
    jobs = get_jobs(last_page)
    print(jobs)


get_stack_over_flow_jobs()
