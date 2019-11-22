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
    print(title)


def get_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        job_summarys = soup.find_all("div", {"class": "-job"})
        for job_summary in job_summarys:
            get_job(job_summary)


def get_stack_over_flow_jobs():
    last_page = get_last_page()
    job_summays = get_jobs(last_page)
    return job_summays


get_stack_over_flow_jobs()
