from lxml import etree
import requests
from openpyxl import Workbook
from bs4 import BeautifulSoup


def get_xml_from_sitemap():
    response = requests.get('https://www.coursera.org/sitemap~www~courses.xml')
    xml_data = response.content
    return xml_data


def get_courses_list(xml, quantity):
    tree = etree.fromstring(xml)
    courses_list = []
    for stick in tree:
        courses_list.append(stick[0].text)
    return courses_list[:quantity]


def get_course_info(course_url):
    response = requests.get(course_url)
    dirty_html = response.content
    soup = BeautifulSoup(dirty_html, 'html.parser')
    course_name = soup.find_all('h2')[0].get_text()
    course_language = soup.find_all('div', 'rc-Language')[0].get_text()
    course_start_date = soup.find_all('div', 'startdate')[0].get_text()
    course_length = len(soup.find_all('div', 'week'))
    try:
        course_ratings = soup.find_all('div', 'ratings-text')[0].get_text()
    except IndexError:
        course_ratings = None
    return {'course_name': course_name,
            'course_language': course_language,
            'course_start_date': course_start_date,
            'course_length': course_length,
            'course_ratings': course_ratings}


def save_courses_info_to_xlsx(courses_info):
    wb = Workbook()
    ws1 = wb.active
    ws1.title = 'Coursera'
    ws1['A1'] = 'Название курса'
    ws1['B1'] = 'Язык курса'
    ws1['C1'] = 'Дата начала курса'
    ws1['D1'] = 'Длительность курса (недели)'
    ws1['E1'] = 'Средняя оценка курса'
    row_nums = [row_num for row_num in range(2, len(courses_info) + 2)]
    for course in courses_info:
        row_num = row_nums.pop()
        ws1['A{}'.format(row_num)] = course['course_name']
        ws1['B{}'.format(row_num)] = course['course_language']
        ws1['C{}'.format(row_num)] = course['course_start_date']
        ws1['D{}'.format(row_num)] = course['course_length']
        if course['course_ratings'] is None:
            ws1['E{}'.format(row_num)] = 'No ratings yet'
        else:
            ws1['E{}'.format(row_num)] = course['course_ratings']
    wb.save(filename='./courses.xlsx')


if __name__ == '__main__':
    print('Collecting data....')
    courses_xml = get_xml_from_sitemap()
    courses_quantity = 10
    courses_list = get_courses_list(courses_xml, courses_quantity)
    courses_info = []
    for course_link in courses_list:
        courses_info.append(get_course_info(course_link))
    save_courses_info_to_xlsx(courses_info)
    print('Complete! Check courses.xlsx!')
