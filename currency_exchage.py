from countries import show_countries, extract_name

lists = show_countries()


def start(lists):
    print("Welcome to CurrencyConvery PRO 2000")
    for i in range(len(lists)):
        print(f"# {i} {extract_name(lists[i])}")


start(lists)
