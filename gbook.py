import os
import sys
import requests
import json


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
    bk = gbooks()
    for line in sys.stdin:
        for i in bk.search(line):
            print(json.dumps(i, indent=4))
