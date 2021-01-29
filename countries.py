import requests
from bs4 import BeautifulSoup

URL = "https://www.iban.com/currency-codes"

# 배열에 국가 별 정보 저장


def show_countries():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    countries = soup.table.find_all('tr')

    lists = []

    for country in countries[1:]:
        info = country.find_all('td')
        # 코드 없는 국가는 제외
        if extract_code(info) != "":
            lists.append(info)
        # 총 265 국가
    return lists

# 국가 코드 추출


def extract_code(list):
    code = list[2].get_text()
    return code

# 국가 명 추출


def extract_name(list):
    name = list[0].get_text()
    return name

# 국가 내역 출력


def start():
    print("Hello! Please choose select a counry by number: ")
    lists = show_countries()
    for i in range(len(lists)):
        print(f"# {i} {extract_name(lists[i])}")


def take_num():
    num = input("#: ")
    return type(num)


take_num()
