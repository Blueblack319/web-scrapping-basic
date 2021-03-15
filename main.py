from bs4 import BeautifulSoup
import requests
import time
from datetime import date

html_text = requests.get(
    "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="
).text
soup = BeautifulSoup(html_text, "html.parser")
jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

print("Put some skill which you are familiar with ")
familiar_skill = input(">")
print(f"Include skill: {familiar_skill}")


def find_jobs():
    with open(f"jobs/{date.today()}.txt", "w") as f:
        for index, job in enumerate(jobs):
            published_date = job.find("span", class_="sim-posted").span.text
            required_skills = job.find("span", class_="srp-skills").text.replace(" ", "")
            if "few" in published_date and familiar_skill in required_skills:
                company_name = job.find("h3", class_="joblist-comp-name").text
                more_info = job.header.h2.a["href"]
                f.write(f"Company Name: {company_name.strip()}\n")
                f.write(f"Required Skills: {required_skills.strip()}\n")
                f.write(f"More Info: {more_info}\n")
        print(f"Save file: {date.today()}.txt")


if __name__ == "__main__":
    while True:
        find_jobs()
        waiting = 1
        print(f"Wainting {waiting} day...")
        time.sleep(waiting * 24 * 60 * 60)
