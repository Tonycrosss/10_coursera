from lxml import etree
import requests
import openpyxl
import bs4


def get_xml_from_sitemap():
    response = requests.get('https://www.coursera.org/sitemap~www~courses.xml')
    xml_data = response.content
    print(str(xml_data.decode('utf-8')))
    return xml_data


def get_courses_list(xml):
    tree = etree.XML(xml)
    # child = tree.getchildren()
    # for c in tree:
    #     print(c.text)
    # nodes = child.xpath('/url/loc')  # Открываем раздел
    # for node in nodes:  # Перебираем элементы
    #     print(node.tag, node.keys(), node.values())
    #     print('name =', node.get('name'))  # Выводим параметр name
    #     print('text =', [node.text])  # Выводим текст элемента


def get_course_info(course_slug):
    pass


def output_courses_info_to_xlsx(filepath):
    pass


if __name__ == '__main__':
    courses_xml = get_xml_from_sitemap()
    courses_list = get_courses_list(courses_xml)
