from requests_html import HTMLSession
from bs4 import BeautifulSoup
import csv
import codecs
import argparse


s = HTMLSession()


def getdata(url: str) -> BeautifulSoup:
    r = s.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    return soup


def scrape_stars(soup: BeautifulSoup) -> list:
    stars = soup.findAll("div", class_="col-12 d-block width-full py-4 border-bottom color-border-muted")
    links = list(map(lambda x: f"https://github.com{x}", [star.div.h3.a["href"] for star in stars]))
    descriptions = [des.p.text.strip() if des.p else "" for des in [star.find("div", class_="py-1") for star in stars]]
    return {link: description for link, description in zip(links, descriptions)}


def write_csv(stars: list, user_name):
    with codecs.open(f"github_stars_{user_name}.csv", "w", "utf-8") as f_obj:
        writer = csv.writer(f_obj)
        writer.writerow(["Link", "Description"])    # header
        for data in stars:
            [writer.writerow([key, value]) for key, value in data.items()]

    print(f"github_stars_{user_name}.csv: Done!!!!")


def get_next_page(soup: BeautifulSoup) -> str | None:
    page = soup.find('div', class_="BtnGroup")
    if page:
        if not page.button.text == "Next" and page.button["disabled"] == "disabled":
            url = page.a["href"] if page.a.text == "Next" else None
            return url
    return None
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Starred Repos Scraping")
    parser.add_argument('-u', '--user_name', type=str, required=True , help='username')
    args = parser.parse_args()
    
    username = args.user_name
    url = f"https://github.com/{username}?tab=stars"

    stars = []
    while True:
        soup = getdata(url)
        stars.append(scrape_stars(soup))
        url = get_next_page(soup)
        if not url:
            break
        print(url)

    write_csv(stars, username)
