import requests

def main():
    base = input('First Currency: ')
    other = input('Second Currency: ')
    res = requests.get('http://api.fixer.io/latest',
                        params={'base': base, 'symbols': other})
    if res.status_code !== 200:
        raise Exception('ERROR: API request unsuccessful.')
    data = res.json()
    rate = data['rates'][other]
    print(f'1 {base} is equal to {rate} {other}')


    # res = requests.get('http://api.fixer.io/latest?base=USD&symbols=EUR')
    # if res.status_code != 200:
    #     raise Exception("ERROR: API request unsuccessful.")
    # data = res.json()
    # rate = data["rates"]['EUR']
    # print(f'1 USD is equal to {rate} EUR')


if __name__ == '__main__':
    main()


# requests.get(url)
# requests.post(url)
# requests.put(url)
# requests.patch(url)
# requests.delte(url)

# Status codes

#  2 in the hundreds place generally means success
# 200 OK
# 201 Created

#  4 in the hundreds place generally means error
# 400 Bad Request
# 403 Forbidden
# 404 Not Found
# 405 Method Not Allowed
# 422 Unprocessable Entity