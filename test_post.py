import requests

index = input()

adr = requests.get(f'https://www.postindexapi.ru/json/{index[:3]}/{index[:3]}{index[3:]}.json')
print(adr.text)
