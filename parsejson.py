import json
import argparse
import sys

"""
    read json from stdin, one json per line
    parse the fields given on the command line
    write to stdout
"""

class ParseJson:
    def __init__(self, data: json, fields: tuple):
        self.data = data
        self.fields = fields

    def write_json(self):
        for field in self.fields:
            print(json.dumps(self.data[field]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('fields', nargs='+')
    args = parser.parse_args()
    for line in sys.stdin:
        data = json.loads(line)
        pj = ParseJson(data, args.fields)
        pj.write_json()