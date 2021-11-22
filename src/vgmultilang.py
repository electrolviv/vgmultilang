#!/usr/bin/python3

import sys
import json
# import yaml

if __name__ != "__main__":
    exit(0)

if len(sys.argv) < 2:
    print("vgmultilang.py <mlangfile.json>")
    exit(0)

jfile = sys.argv[1]

print("Processing file : " + jfile)

# Load JSON file
with open(jfile) as json_file:
    data = json.load(json_file)
    print(data)

# from yaml import load, dump
# try:
#     from yaml import CLoader as Loader, CDumper as Dumper
# except ImportError:
#     from yaml import Loader, Dumper
#
# # ...
#
# data = load(stream, Loader=Loader)
#
# # ...
#
# output = dump(data, Dumper=Dumper)
