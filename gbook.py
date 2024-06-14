from os import environ
import sys
import requests
import json
import argparse

class gbooks():

    googleapikey: str = environ.get('googleapikey')
    googlebookapi: str = "https://www.googleapis.com/books/v1/volumes"


    def search(self, value: str) -> iter:
        params: dict = {"q": value, 'key': self.googleapikey}
        r: requests.Response = requests.get(url=self.googlebookapi, params=params)
        rj: json = r.json()
        try:
            for i in rj["items"]:
                yield i["volumeInfo"]
        except:
            pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='gbook.py', description='Search Google Books', epilog='Example: echo test | gbook.py -pretty')
    parser.add_argument('-p', '--pretty', help='pretty print the output', required=False, action='store_true')
    args = parser.parse_args()
    books = gbooks()
    for line in sys.stdin:
        for book in books.search(line):
            if args.pretty:
                print(json.dumps(book, indent=4))
            else:
                print(repr(book))
