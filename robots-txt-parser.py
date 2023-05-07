import requests
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-u", "--useragent", help="User Agent")
parser.add_argument("-host", "--host", help="Webiste Url")


def parse():
    url = "http://www.tripadvisor.com/robots.txt"
    headers = {
    'User-Agent': 'bugcrowd',
    }
    res = requests.get(url, headers=headers)
    
    print(res.text)

parse()