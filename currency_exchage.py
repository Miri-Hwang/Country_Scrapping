from countries import show_countries, extract_name, take_num, extract_code
import requests
import os
from bs4 import BeautifulSoup


lists = show_countries()


def start(lists):
    print("Welcome to CurrencyConvery PRO 2000")
    for i in range(len(lists)):
        print(f"# {i} {extract_name(lists[i])}")

# take nums without limits


def take_amounts():
    while True:
        try:
            num = int(input("#: "))
            return num
            break
        except ValueError:
            print("That wasn't a number")

# Let user choose country a & b , and amounts of money to exchange.


def take_inputs():
    print("Where are you from? Choose a country by number.\n\n")
    a = take_num()
    a_name = extract_name(lists[a])
    a_code = extract_code(lists[a])
    print(f"{a_name}\n\n")

    print("Now choose another country.")
    b = take_num()
    b_name = extract_name(lists[b])
    b_code = extract_code(lists[b])
    print(f"{b_name}\n\n")

    print(
        f"How many {a_code} do you want to convert to {b_code}?")
    amounts = take_amounts()
    return {'a_name': a_name, 'a_code': a_code, 'b_name': b_name, 'b_code': b_code, 'amounts': amounts}


# Get an Exchange Rate from Country a to Country b in the dict
def get_rate(dict):
    URL = f"https://transferwise.com/gb/currency-converter/{dict['a_code']}-to-{dict['b_code']}-rate?amount={dict['amounts']}"
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, "html.parser")
    calculator = soup.find('div', {'class': 'js-Calculator'}).find('form')
    rate = calculator.find('h3', {
                           'class': 'cc__source-to-target'}).find('span', {'class': 'text-success'}).string
    rate = str(rate.encode('utf-8')).strip('b').replace("'", "")
    return rate

# Get Result


def get_result():
    inputs = take_inputs()
    a = inputs['a_code']
    b = inputs['b_code']
    amounts = float(inputs['amounts'])
    amounts_format = "{:,.2f}".format(amounts)
    rate = float(get_rate(inputs))
    result = "{:,}".format(int(amounts * rate))
    print(f"{a}{amounts_format} is {b}{result}")


start(lists)
get_result()
