import os
import sys
import requests
import json
import argparse

class gbooks():
    googleapikey = os.environ.get('googleapikey')

    def search(self, value: object) -> object:
        parms = {"q": value, 'key': self.googleapikey}
        r = requests.get(url="https://www.googleapis.com/books/v1/volumes", params=parms)
        rj = r.json()
        try:
            for i in rj["items"]:
                yield i["volumeInfo"]
        except:
            pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='gbook.py', description='Search Google Books', epilog='Example: gbook.py -q "Book"')
    parser.add_argument('-p', '--pretty', help='pretty print the output', required=False, action='store_true')
    args = parser.parse_args()
    bk = gbooks()
    for line in sys.stdin:
        for i in bk.search(line):
            if args.pretty:
                print(json.dumps(i, indent=4))
            else:
                print(repr(i))
