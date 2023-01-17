from bs4 import BeautifulSoup

path = r'\\10.88.22.128\dbs\bson\Для Саши Б\test.xls'
to_file = r'\\10.88.22.128\dbs\bson\Для Саши Б\test_out.csv'

with open(path, encoding='utf8') as f:
    soup = BeautifulSoup(f.read(), 'xml')

with open(to_file, 'w') as out:
    for now in soup.find_all('ss:Data'):
        temp = now.get_text()
        if any(True for i in (range(10)) if str(i) in temp) and len(temp) >= 10 and temp.isdigit() and '.' not in temp:
            print(temp)
            out.write(f'{temp}\n')
