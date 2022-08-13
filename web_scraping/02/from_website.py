from bs4 import BeautifulSoup
import requests

html_text = requests.get(
    'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=&cboWorkExp1=0').text

soup: BeautifulSoup = BeautifulSoup(html_text, 'lxml')

jobs = soup.findAll('li', class_="clearfix job-bx wht-shd-bx")

company_names = [job.find('h3', class_='joblist-comp-name').text.strip() for job in jobs]

skills = [job.find('span', class_='srp-skills').text.strip() for job in jobs]

more_infos = [job.header.h2.a['href'] for job in jobs]

published_dates = [job.find('span', class_='sim-posted').span.text.strip() for job in jobs]

[print(p) for p in more_infos]

# for c, s in zip(company_names, skills):
#     print(f"{c}\n{s}\n")
