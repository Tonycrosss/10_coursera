from lxml import etree
import requests
import openpyxl
from bs4 import BeautifulSoup

def get_xml_from_sitemap():
    response = requests.get('https://www.coursera.org/sitemap~www~courses.xml')
    xml_data = response.content
    return xml_data


def get_courses_list(xml, quantity):
    tree = etree.fromstring(xml)
    courses_list = []
    for item in tree:
        courses_list.append(item[0].text)
    return courses_list[:quantity]


def get_course_info(course_slug):
    response = requests.get(course_slug)
    dirty_html = response.content
    soup = BeautifulSoup(dirty_html, 'html.parser')
    course_name = soup.find_all('h2')[0].get_text()
    course_language = soup.find_all('div', 'rc-Language')[0].get_text()
    course_start_date = soup.find_all('div', 'startdate')[0].get_text()
    course_length = len(soup.find_all('div', 'week'))
    try:
        course_ratings = soup.find_all('div', 'ratings-text')[0].get_text()
    except IndexError:
        course_ratings = 'No ratings yet'


def output_courses_info_to_xlsx(filepath):
    pass


if __name__ == '__main__':
    # courses_xml = get_xml_from_sitemap()
    # courses_quantity = 10
    # courses_list = get_courses_list(courses_xml, courses_quantity)
    # print(courses_list)
    get_course_info('https://www.coursera.org/learn/gamification')