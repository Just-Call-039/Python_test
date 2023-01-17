import io

path = r'\\10.88.22.128\dbs\bson\Для Саши Б\test.xls'
k = 0

with io.open(path, 'rb') as file:
    for line in file:
        try:
            print(line.decode("utf-8"))
        finally:
            k += 1
            if k == 100:
                break
    # print(file.readline())
