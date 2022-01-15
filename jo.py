#!/usr/bin/python

import json
from posixpath import split
import sys
import re
import optparse

def recursive_set(root, k, v):
  comps = k.split(".")
  comp = comps[0]
  if len(comps) == 1:
    root[comp] = v
  else:
    d = root.get(comp, {})
    recursive_set(d, ".".join(comps[1:]), v)
    root[comp] = d

# TODO:: add a --sep flag to control the "."
# TODO:: add a way to specify the type of a value (int/bool)
# TODO:: add a way to add a timestamp in s and ms

def main():
  desc = """
  Process the stdin line by line. apply the following operators on each line.
  """
  parser = optparse.OptionParser(description = desc)
  parser.add_option("", "--version",
                    action="store_true",
                    help="print version number",
                    dest="version",
                    default=False)
  parser.add_option("", "--Splice",
                    type=str,
                    help="Output the given RE",
                    dest="splice",
                    default=None)
  (options, vars) = parser.parse_args()

  if options.version:
    print("0.2")
    sys.exit(0)

  root = {}
  for kv in vars:
    k = kv.split("=")[0]
    v = kv.split("=")[1]
    recursive_set(root, k, v)

  print(json.dumps(root, sort_keys=True))
if __name__ == "__main__":
  main()
