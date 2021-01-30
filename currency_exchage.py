from countries import show_countries, extract_name, take_num, extract_code

lists = show_countries()


def start(lists):
    print("Welcome to CurrencyConvery PRO 2000")
    for i in range(len(lists)):
        print(f"# {i} {extract_name(lists[i])}")

# Let user choose country a & b , and amounts of money to exchange.


def take_inputs():
    print("Where are you from? Choose a country by number.\n\n")
    a = take_num()
    print(f"{extract_name(lists[a])}\n\n")
    print("Now choose another country.")
    b = take_num()
    print(f"{extract_name(lists[b])}\n\n")

    print(
        f"How many {extract_code(lists[a])} do you want to convert to {extract_code(lists[b])}?")
    amounts = take_num()
    return {'a': a, 'b': b, 'amounts': amounts}


start(lists)
print(take_inputs())
