from bs4 import BeautifulSoup

import xml.etree.ElementTree as ET
import requests as req

path = r'\\10.88.22.128\dbs\bson\Для Саши Б\test.xls'
soup = BeautifulSoup(open(path, encoding='utf8').read(), 'xml')

b_unique = soup.find_all('unique')

print(b_unique)
print(soup.text)


# print(soup.prettify())

# def extract_data_from_report3(filename):
#     soup = BeautifulSoup(open(filename), "html.parser")
