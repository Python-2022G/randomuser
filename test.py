import requests
from datetime import datetime


while True:
    response = requests.get('https://randomuser.me/api/')
    if response.status_code == 200:
        user = response.json()['results'][0]
        dt = user['dob']['date']
        dat = datetime.strptime(dt[:-5], '%Y-%m-%dT%H:%M:%S') #1958-02-09T05:22:53.242Z
        if dat.year in [1990, 1980, 1989, 1991, 1977, 1968]:
            print(dat)
            break