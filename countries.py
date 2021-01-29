import requests
from bs4 import BeautifulSoup

URL = "https://www.iban.com/currency-codes"


def show_countries():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    countries = soup.table.find_all('tr')

    lists = []

    for country in countries[1:]:
        info = country.find_all('td')

        if extract_code(info) != "":
            lists.append(info)

    return lists


def extract_code(list):
    code = list[2].get_text()
    return code


print(show_countries())
