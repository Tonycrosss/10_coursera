from lxml import etree
import requests
import openpyxl
import bs4


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
    pass


def output_courses_info_to_xlsx(filepath):
    pass


if __name__ == '__main__':
    courses_xml = get_xml_from_sitemap()
    courses_quantity = 10
    courses_list = get_courses_list(courses_xml, courses_quantity)
    print(courses_list)
