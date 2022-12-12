import requests


while True:
    response = requests.get('https://randomuser.me/api/')
    if response.status_code == 200:
        user = response.json()['results'][0]
        age = int(user['dob']['date'][:4])
        if age in [1990, 1980, 1999, 1977, 1989, 1990]:
            name = user['name']['first']
            print(name, age)
