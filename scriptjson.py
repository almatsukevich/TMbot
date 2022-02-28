import requests

url = 'https://www.wildberries.ru/catalog/18409417/detail.aspx'
res = requests.get(url)
jsonf = res.json()

