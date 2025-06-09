import json
from urllib.request import urlopen

def define_gender(name):
    myKey = "b486d9ed5fc81339a5295087f4f14534e13d9034faaa6bad19bd1d6064f33c75"
    url = "https://gender-api.com/get?key=" + myKey + f"&name=^{name}"
    response = urlopen(url)
    decoded = response.read().decode('utf-8')
    data = json.loads(decoded)
