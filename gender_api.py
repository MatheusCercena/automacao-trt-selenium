import json
from urllib.request import urlopen

def define_gender(name):
    name = name.strip().split()[0]
    myKey = "b486d9ed5fc81339a5295087f4f14534e13d9034faaa6bad19bd1d6064f33c75"
    url = f"https://gender-api.com/get?key={myKey}&name={name}"
    response = urlopen(url)
    decoded = response.read().decode('utf-8')
    data = json.loads(decoded)['gender']
    if data == 'male':
        return 'M' 
    else:
        return 'F'
