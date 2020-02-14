import requests


def base(cur):
    url = "https://api.exchangerate-api.com/v4/latest/" + cur
    response = requests.get(url)
    return response.json()


def print_cur():
    data = base(input("Enter the base currency:").lower())
    print('List of all CURRENCIES:')
    for key, val in data['rates'].items():
        print(key)
    curr = input("Enter the required currency:").upper()
    for cur, rate in data['rates'].items():
        if cur == curr:
            print("________________")
            print(cur, rate)


print_cur()
