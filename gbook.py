import os
import sys
import requests


class gbooks():
    googleapikey = os.environ.get('googleapikey')

    def search(self, value: object) -> object:
        parms = {"q": value, 'key': self.googleapikey}
        r = requests.get(url="https://www.googleapis.com/books/v1/volumes", params=parms)
        rj = r.json()
        try:
            for i in rj["items"]:
                print(repr(i["volumeInfo"]["title"]))
                print(repr(i["volumeInfo"]["authors"]))
                print(repr(i["volumeInfo"]["description"]))
                print('-'*80)
        except:
            pass


if __name__ == "__main__":
    bk = gbooks()
    for line in sys.stdin:
        bk.search(line)
