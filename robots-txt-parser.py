import requests

def parse():
    url = "http://www.tripadvisor.com/robots.txt"
    headers = {
    'User-Agent': 'bugcrowd',
    }
    res = requests.get(url, headers=headers)
    
    print(res.text)

parse()