from bs4 import BeautifulSoup
from bs4.element import ResultSet

with open('index.html', 'r') as html_file:
    content = html_file.read()

    soup: BeautifulSoup = BeautifulSoup(content, 'lxml')

    '''
    courses_html_tags: ResultSet = soup.findAll('h5')
    [print(course.text) for course in courses_html_tags]
    '''

    course_cards = soup.findAll('div', class_='card')

    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        print(f"{course_name} is of price: {course_price}")
