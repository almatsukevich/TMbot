import requests
from bs4 import BeautifulSoup
import pandas
from pandas import ExcelWriter
import openpyxl
import lxml


def get_html(url, params=None):
    """html код страницы"""
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0",
    }
    html = requests.get(url, headers=headers, params=params)
    return html


def get_content(html, num):
    """сбор контента со страницы"""
    soup = BeautifulSoup(html.text, 'html.parser')
    quotes1 = soup.find_all('div', class_='same-part-kt__header-wrap hide-mobile')
    quotes2 = quotes1[0].find_all('span')
    if num == 1:
        answ = quotes2[0].text
        return answ
    else:
        answ = quotes2[1].text
        return answ



def parser(url, num):
    html = get_html(url)
    if html.status_code == 200:
        html = get_html(url)
        answ = get_content(html, num)
        return answ
    else:
        return "Такого товара не существует"


if __name__ == "__main__":
    parser('https://www.wildberries.ru/catalog/18409417/detail.aspx', 2)
    
