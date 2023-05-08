import requests
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-u", "--useragent", dest= "useragent", help="User Agent")
parser.add_argument("-host", "--host", dest="host", help="Webiste Url")

args = parser.parse_args()

def parse():
    url = args.host + "/robots.txt"
    headers = {
    'User-Agent': args.useragent,
    }
    res = requests.get(url, headers=headers)
    
    response_content = res.text
    response_parsed = ""

    for line in response_content.splitlines():
        if not line.startswith("User-Agent:") and not len(line.strip()) == 0:
            response_parsed += line.replace("Disallow: ", args.host).replace("Allow: ", args.host) + "\n"

    print(response_parsed)

parse()