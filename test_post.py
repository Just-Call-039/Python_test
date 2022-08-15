import requests

index = input()

adr = requests.get(f'https://www.postindexapi.ru/json/{index[:3]}/{index[:3]}{index[3:]}.json')
print(type(adr), adr)

try:
    full_adr = adr.json()
    print(full_adr)
    my_city = full_adr['City']
    my_region = full_adr['Region']
    if not my_city or my_city == '' or my_city == ' ':
        my_city = 0
    if not my_region or my_region == '' or my_region == ' ':
        my_region = 0
    print(my_city)
    print(my_region)
except (requests.exceptions.ConnectionError, ValueError):
    print(0)
