import pandas as pd
import os
import time

from bs4 import BeautifulSoup
from commons.convert_time import convert_time

print(f'Время начала: {time.ctime()}')
print()

path = r'\\10.88.22.128\dbs\bson\файлы xls'
out = r'\\10.88.22.128\dbs\bson\файлы xls\out'
temp = r'\\10.88.22.128\dbs\bson\файлы xls\temp'

# print(*[i for i in os.listdir(path) if i.endswith('.xls' or '.xml')], sep='\n')
list_files = os.listdir(path)

for i in list_files:
    start_time = time.time()
    if i.endswith('.xls' or '.xml'):
        full_path = f'{path}\\{i}'
        temp_path = f'{temp}\\{i.rstrip(".xls")}_temp.csv'
        out_path = f'{out}\\{i.rstrip(".xls")}_out.csv'

        # print(full_path)
        # print(temp_path)
        # print(out_path)

        with open(full_path, encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'xml')

        with open(temp_path, 'w', encoding='utf-8') as temp_file:
            for now in soup.find_all('ss:Data'):
                temp_text = now.get_text()
                if any(True for i in (range(10)) if str(i) in temp_text) and len(temp_text) >= 10 \
                        and temp_text.isdigit() and '.' not in temp_text:
                    temp_file.write(f'{temp_text}\n')

        df = pd.read_csv(temp_path, header=None)
        df = df[0].unique()
        df = pd.Series(df)
        df.to_csv(out_path, sep=';', header=False)

        # os.remove(to_file)

        end_time = time.time()

        print(f'На файл {out_path} ушло времени: {convert_time(end_time - start_time)}', end=' ')

print()
print(f'Время окончания: {time.ctime()}')
