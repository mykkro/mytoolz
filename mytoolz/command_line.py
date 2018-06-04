from collections import OrderedDict

from mytoolz import hello, remove_accents, load_json_data, save_json_data
import sys, json, pyaml


def main():
    print(hello())


def remove_accents_cli():
    txt = sys.argv[1] if len(sys.argv)>1 else ""
    print(remove_accents(txt))


def format_json_cli():
    path = sys.argv[1]
    with open(path, "r") as infile:
        data = json.load(infile, object_pairs_hook = OrderedDict)
    if len(sys.argv) > 2:
        outpath = sys.argv[2]
        save_json_data(data, outpath)
    else:
        print json.dumps(data, indent=4)
