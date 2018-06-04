from mytoolz import hello, remove_accents
import sys, json, pyaml


def main():
    print(hello())


def remove_accents_cli():
    txt = sys.argv[1] if len(sys.argv)>1 else ""
    print(remove_accents(txt))

