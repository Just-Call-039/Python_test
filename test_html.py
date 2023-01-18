import pandas as pd
import os

from bs4 import BeautifulSoup

path = r'\\10.88.22.128\dbs\bson\Для Саши Б\test.xls'
# to_file = r'\\10.88.22.128\dbs\bson\Для Саши Б\test_out.csv'
# print(os.path.abspath('test.xls'))
to_file = rf'\temp\{path.rstrip(".csv")}_temp.csv'
# to_file_end = r'\\10.88.22.128\dbs\bson\Для Саши Б\test_end.csv'
to_file_end = rf'\out\{path.rstrip(".csv")}_out.csv'

with open(path, encoding='utf8') as f:
    soup = BeautifulSoup(f.read(), 'xml')

with open(to_file, 'w') as out:
    for now in soup.find_all('ss:Data'):
        temp = now.get_text()
        if any(True for i in (range(10)) if str(i) in temp) and len(temp) >= 10 and temp.isdigit() and '.' not in temp:
            # print(temp)
            out.write(f'{temp}\n')

df = pd.read_csv(to_file, header=None)
# print(df.head())
# print(df.info)
# df = df.drop_duplicates(subset=0)
df = df[0].unique()
# print(len(df))
df = pd.Series(df)
df.to_csv(to_file_end, sep=';', header=False)

os.remove(to_file)

print('Done.')
